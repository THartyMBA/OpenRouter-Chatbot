# chat_app.py
"""
Streamlit ▸ OpenRouter Chatbot with Memory 🤖🧠
----------------------------------------------
• Uses **any free OpenRouter model** (default: `mistralai/mistral-7b-instruct`).  
• Remembers the full conversation in `st.session_state`.  
• Requires your **OpenRouter API key** in an env-var called `OPENROUTER_API_KEY`
  **or** in `st.secrets["OPENROUTER_API_KEY"]`.

Run locally:
    streamlit run chat_app.py
Deploy for free on Streamlit Cloud (private repo works too).
"""

import os
import requests
import streamlit as st

OPENROUTER_API_KEY = (
    st.secrets.get("OPENROUTER_API_KEY")
    or os.getenv("OPENROUTER_API_KEY")
    or ""
)

# ────────────────────────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────────────────────────
def send_chat_completion(messages, model="mistralai/mistral-7b-instruct", temperature=0.7):
    """Call the OpenRouter /chat/completions endpoint and return the assistant reply."""
    if not OPENROUTER_API_KEY:
        raise RuntimeError(
            "OpenRouter API key missing – set OPENROUTER_API_KEY env variable "
            "or add it to st.secrets."
        )

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # One of these two headers is required by OpenRouter.
        # Feel free to change to your own domain/title.
        "HTTP-Referer": "https://your-portfolio-site.example",
        "X-Title": "StreamlitChatDemo",
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    res = requests.post(url, headers=headers, json=payload, timeout=60)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]


def init_session():
    if "messages" not in st.session_state:
        # Seed with a system prompt – adjust personality here
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]


# ────────────────────────────────────────────────────────────────────────────────
# Streamlit UI
# ────────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="🗣️ OpenRouter Chatbot", layout="wide")
st.title("🗣️ Free-Model Chatbot (OpenRouter)")
st.info(
    "🔔 **Demo Notice**  \n"
    "This application is a streamlined proof-of-concept, **not** an "
    "enterprise-grade product.  \n\n"
    "Need production-level performance, security or custom features? "
    "[Get in touch](mailto:you@example.com) and let’s build a tailored solution.",
    icon="💡",
)

init_session()

with st.sidebar:
    st.header("Settings ⚙️")
    model = st.selectbox(
        "OpenRouter model",
        options=[
            "mistralai/mistral-7b-instruct",          # free
            "thu-dongfang/zephyr-7b-beta",            # free
            "undi95/toppy-m-7b",                      # free
            "thebloke/neural-chat-7b-v3-1",           # free
            "google/gemma-7b-it"                      # free
        ],
        index=0,
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
    if st.button("🧹 Clear chat"):
        st.session_state.messages = st.session_state.messages[:1]  # keep system prompt

# Show chat history
for msg in st.session_state.messages[1:]:  # skip system prompt when displaying
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input box (Streamlit 1.32+ has st.chat_input)
user_input = st.chat_input("Type a message…")
if user_input:
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Call OpenRouter
    with st.spinner("Thinking…"):
        try:
            assistant_reply = send_chat_completion(
                st.session_state.messages, model=model, temperature=temperature
            )
        except Exception as e:
            st.error(f"API error: {e}")
            st.stop()

    # Append assistant reply & display
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.chat_message("assistant").markdown(assistant_reply)
