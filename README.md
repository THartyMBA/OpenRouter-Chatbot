# OpenRouter-Chatbot
🗣️ Memory-Powered Chatbot (OpenRouter Edition)
A minimalist Streamlit chat interface that wraps any free OpenRouter model and remembers the conversation for the entire browser session.

✨ Features

Capability	Details
Conversational memory	Stores messages in st.session_state and sends full history on every turn.
Plug-and-play model	Default mistralai/mistral-7b-instruct, but you can pick any free OpenRouter model from the sidebar.
Adjustable creativity	Temperature slider (0 – 1).
Clear chat	One-click reset keeps the system prompt but drops user/assistant turns.
100 % client-side UI	Single Python file, no backend server needed.
Proof-of-concept – no auth, persistence, or rate-limit handling.
For production LLM chat (RAG, caching, SSO), contact drtomharty.com/bio.

🔑 Add your OpenRouter API key
Streamlit Cloud (recommended)
Deploy the repo → ⋯ ➜ Edit secrets

Insert:

toml
Copy
Edit
OPENROUTER_API_KEY = "sk-or-xxxxxxxxxxxxxxxx"
Local development
Create ~/.streamlit/secrets.toml:

toml
Copy
Edit
OPENROUTER_API_KEY = "sk-or-xxxxxxxxxxxxxxxx"
—or set an env-var:

bash
Copy
Edit
export OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
🚀 Quick start
bash
Copy
Edit
git clone https://github.com/yourname/openrouter-chatbot.git
cd openrouter-chatbot-demo
python -m venv venv && source venv/bin/activate      # Win: venv\Scripts\activate
pip install -r requirements.txt
streamlit run chat_app.py
Open http://localhost:8501 in your browser and start chatting.

☁️ Zero-cost deployment on Streamlit Cloud
Push the repo (public or private) to GitHub.

Go to streamlit.io/cloud ➜ New App and select the repo/branch.

Add the OPENROUTER_API_KEY in Secrets.

Click Deploy – done!

🗂️ File structure
Copy
Edit
chat_app.py          ← the entire app
requirements.txt
README.md            ← you’re here
🛠️ Requirements
shell
Copy
Edit
streamlit>=1.32
requests
(The models are served remotely by OpenRouter, so no heavy ML libs are required.)

📜 License
CC0 – do whatever you like; attribution always appreciated.

🙏 Acknowledgements
OpenRouter – unified gateway to open LLMs

Streamlit – trivial web apps for Python

Enjoy the chat! 🎉
