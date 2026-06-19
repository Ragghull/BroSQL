# BroSQL AI — Streamlit + Gemini SQL Companion

BroSQL AI is a sleek, modern SQL companion designed to help you debug, explain, optimize, generate SQL queries, roast your code, and prepare for SQL interviews.

## Stack
- Python 3.10+
- Streamlit
- Google Gemini API (google-generativeai)
- Deployment: Streamlit Community Cloud

## File Structure
```
brosql-ai/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── README.md
```

## Running Locally

1. Clone the repository (or navigate to the workspace directory).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API Key (see section below).
4. Start Streamlit:
   ```bash
   streamlit run app.py
   ```

## Setting up your Gemini API Key

1. Get your free key at: https://makersuite.google.com/app/apikey
2. Open .streamlit/secrets.toml
3. Replace "paste-your-gemini-key-here" with your actual key
4. Save the file
5. Run: streamlit run app.py

The key is stored locally only. Never commit secrets.toml to GitHub.

## Deployment to Streamlit Community Cloud

1. Push your code to a public GitHub repository.
2. Visit share.streamlit.io.
3. Connect your GitHub repository.
4. Set the main file path to: app.py.
5. Under App settings -> Secrets, add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your-actual-gemini-api-key"
   ```
6. Click Deploy!
