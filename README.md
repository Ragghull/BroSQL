# **BroSQL AI — AI-Powered SQL Copilot**

> *"Your intelligent SQL companion that writes, debugs, explains, and roasts your queries in real time."*

---

## **What is BroSQL AI?**

*BroSQL AI is a modern AI-powered SQL assistant built with **Streamlit + OpenRouter API** that helps developers and students level up their SQL skills — fast, fun, and without the fluff.*

*Whether you are a complete beginner struggling with JOINs or a senior dev optimizing a slow query, BroSQL AI has your back.*

---

## **Key Features**

### **SQL Intelligence Engine**
*Fix broken queries instantly. Detect logical and syntax issues. Suggest optimized SQL patterns — all powered by AI reasoning.*

### **Explain Like I'm 5 Mode**
*Converts complex SQL into simple, beginner-friendly explanations. Step-by-step breakdown of how your query actually executes.*

### **Query Generator**
*Describe what you need in plain English. BroSQL AI writes the SQL for you — SELECT, JOIN, GROUP BY, subqueries and more.*

### **Interview Prep Mode**
*Practice SQL interview questions. Get AI-generated hints, answers, and tips on what interviewers actually look for.*

### **Roast Mode — Fan Favourite**
*AI humorously critiques your messy SQL. One savage roast. Then full professional explanation. Learning has never been this entertaining.*

---

## **Architecture**

```
User Input (SQL or Plain English)
           ↓
  Streamlit Frontend
           ↓
  Prompt Engineering Layer
           ↓
  OpenRouter API  →  Free AI Model
           ↓
  Structured AI Response
           ↓
  Rendered Output (Fix / Explain / Roast)
```

---

## **Project Structure**

```
brosql-ai/
├── app.py                  ← Single file app, all logic here
├── requirements.txt        ← Python dependencies
├── .gitignore              ← secrets.toml excluded
├── .streamlit/
│   ├── config.toml         ← Light cyan theme config
│   └── secrets.toml        ← YOUR API KEY (never push this)
└── README.md
```

---

## **Getting Started**

### **Step 1 — Clone the Repository**

```bash
git clone https://github.com/your-username/brosql-ai.git
cd brosql-ai
```

### **Step 2 — Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3 — Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4 — Add Your API Key**

*Get your free OpenRouter API key at:* ***https://openrouter.ai/keys***

*Open `.streamlit/secrets.toml` and add:*

```toml
OPENROUTER_API_KEY = "sk-or-v1-your-actual-key-here"
```

> **Important:** *The app will NOT work without a valid API key. Never commit `secrets.toml` to GitHub — it is already excluded in `.gitignore`.*

### **Step 5 — Run the App**

```bash
streamlit run app.py
```

*Your browser will open automatically at `http://localhost:8501`*

---

## **Deployment — Streamlit Community Cloud**

*Deploy your own live version in under 5 minutes:*

1. *Push this repository to GitHub (make sure `secrets.toml` is in `.gitignore`)*
2. *Go to* ***https://share.streamlit.io***
3. *Click **New App** → Select your repository*
4. *Set entry file →* `app.py`
5. *Go to **Advanced Settings** → **Secrets** → Add:*

```toml
OPENROUTER_API_KEY = "sk-or-v1-your-actual-key-here"
```

6. *Click **Deploy** — done.*

---

## **API Note**

*BroSQL AI uses the **OpenRouter free tier** which provides access to powerful open-source models at no cost.*

*Each user provides their own API key — this keeps the project open, fair, and scalable for everyone.*

*Free models used:*
- *`google/gemma-2-9b-it:free`*
- *`meta-llama/llama-3.2-3b-instruct:free`*
- *`microsoft/phi-3-mini-128k-instruct:free`*

*The app automatically falls back to the next available model if one is unavailable.*

---

## **Why This Project Stands Out**

*Unlike generic AI chatbots, BroSQL AI is laser-focused on one real-world problem — helping developers actually learn and improve SQL.*

| *Feature* | *What it proves* |
|---|---|
| *AI-powered debugging* | *Real-world LLM integration* |
| *Natural language to SQL* | *Strong prompt engineering skills* |
| *Roast Mode* | *Creative product thinking* |
| *Interview Prep* | *Educational value beyond just fixing* |
| *No database, no backend* | *Rapid lightweight prototyping* |

*Built during a **Google AI Bootcamp** as a rapid prototype — demonstrating that great AI products do not need complex infrastructure.*

---

## **Future Scope**

**Version 2**
*SQL syntax highlighting, support for MySQL / PostgreSQL / SQL Server, downloadable AI explanations*

**Version 3**
*VS Code Extension, Browser Extension, LeetCode SQL integration*

**Version 4**
*Connect to a real database, execute queries safely, visual query execution plans, AI-generated indexes*

---

## **Open Source**

*Feel free to:*
- ***Fork it** and make it your own*
- ***Improve it** with new features*
- ***Extend it** with more AI modes*
- ***Make the Roast Mode even more savage***

---

## **The Final Vibe**

> *"BroSQL AI isn't just a tool — it's your SQL partner that fixes your queries, explains the concepts, preps you for interviews, and judges your bad SQL silently."*

---

**If this project helped you — drop a star. It means a lot.**
