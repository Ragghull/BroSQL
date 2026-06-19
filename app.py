import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(
    page_title="BroSQL AI",
    page_icon=None,
    layout="wide"
)

# Custom Premium CSS Injection (Light Theme + Cyan Glassmorphism + Always-on Sidebar)
st.markdown(
    """
    <style>
    /* General page styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e0f7fa 0%, #f0f9ff 50%, #e8f4fd 100%) !important;
        color: #0e4f5c !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        min-height: 100vh;
    }
    
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }

    [data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        width: 300px !important;
        min-width: 300px !important;
        background: rgba(240, 249, 255, 0.85) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(6, 182, 212, 0.2) !important;
    }

    [data-testid="stSidebar"][aria-expanded="false"] {
        display: block !important;
        margin-left: 0 !important;
        transform: none !important;
    }

    [data-testid="collapsedControl"] {
        display: flex !important;
        background: #0891b2 !important;
        color: white !important;
        border-radius: 0 8px 8px 0 !important;
        width: 32px !important;
        height: 48px !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        z-index: 999 !important;
    }

    /* Base headers and labels */
    h1, h2, h3, p, span, label {
        color: #0e4f5c !important;
    }
    
    [data-testid="stWidgetLabel"] p {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #0e4f5c !important;
    }

    /* Page Title (BroSQL AI) */
    .main-header {
        color: #0891b2 !important;
        font-weight: 800;
        font-size: 2.2rem;
        letter-spacing: -0.5px;
        margin-bottom: 2px;
        line-height: 1.2;
    }

    .main-subheader {
        color: #64748b;
        font-size: 1rem;
        margin-top: 0px;
        margin-bottom: 30px;
    }

    /* Text inputs and text areas */
    textarea, input {
        background: rgba(255, 255, 255, 0.7) !important;
        border: 1px solid #a5f3fc !important;
        border-radius: 8px !important;
        color: #0e4f5c !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
    }

    textarea:focus, input:focus {
        border-color: #0891b2 !important;
        box-shadow: 0 0 8px rgba(8, 145, 178, 0.3) !important;
    }

    /* Glassmorphism Main Content Cards */
    div[data-testid="stVerticalBlockBorder"] {
        background: rgba(255, 255, 255, 0.55) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.7) !important;
        box-shadow: 0 8px 32px rgba(6, 182, 212, 0.10) !important;
        padding: 24px !important;
    }
    
    div[data-testid="stVerticalBlockBorder"]:hover {
        border-color: rgba(8, 145, 178, 0.4) !important;
    }

    /* Copy code container styling overrides */
    code {
        color: #0891b2 !important;
        background-color: #e0f7fa !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        font-family: 'Fira Code', 'Courier New', Courier, monospace !important;
        font-size: 0.9em !important;
    }

    pre code {
        color: #0e4f5c !important;
        background-color: transparent !important;
        padding: 0 !important;
    }

    /* Buttons (st.button) */
    div.stButton > button {
        background: #0891b2 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        padding: 12px 24px !important;
        transition: background 0.2s, transform 0.2s !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background: #0e7490 !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(8, 145, 178, 0.2) !important;
    }

    div.stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Radio buttons and labels */
    .stRadio label {
        font-size: 1.05rem !important;
        color: #0e4f5c !important;
        padding: 6px 0 !important;
    }
    
    /* Hide standard Streamlit header and footer styling overlays */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Webkit scrollbar customization */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f0f9ff;
    }
    ::-webkit-scrollbar-thumb {
        background: #0891b2;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #0e7490;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Gemini API helper function using gemini-2.0-flash (exact code block from CHANGE 2)
def get_gemini_response(api_key, system_prompt, user_prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_prompt
    )
    response = model.generate_content(user_prompt)
    return response.text

# Initialize Session State
if "response" not in st.session_state:
    st.session_state.response = ""
if "mode" not in st.session_state:
    st.session_state.mode = "Debug SQL"
if "roast_on" not in st.session_state:
    st.session_state.roast_on = False

# Sidebar Content setup in the exact order requested
st.sidebar.title("BroSQL AI")
st.sidebar.caption("Bro, lets fix your SQL.")
st.sidebar.divider()

# API Key loading logic
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    if not api_key or api_key == "paste-your-gemini-key-here":
        raise ValueError("Placeholder key")
    st.sidebar.success("API key loaded")
except Exception:
    st.sidebar.error(
        "API key missing. Add it to .streamlit/secrets.toml"
    )
    st.stop()

st.sidebar.divider()

# Mode selection
st.sidebar.subheader("Select Mode")
selected_mode = st.sidebar.radio(
    label="",
    options=[
        "Debug SQL",
        "Explain SQL",
        "Optimize SQL",
        "Generate SQL",
        "Be Honest Bro",
        "Interview Tips"
    ],
    key="mode"
)
st.sidebar.divider()

# Roast mode toggle
st.sidebar.subheader("Roast Mode")
roast_on = st.sidebar.toggle("Enable Roast Mode", key="roast_on")
st.sidebar.caption(
    "When ON, adds a roast before every response."
)

# Main Area Layout
st.info(
    "Sidebar hidden? Click the arrow button ( > ) "
    "at the top left to open it. "
    "Your mode options are inside."
)

st.markdown('<div class="main-header">BroSQL AI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subheader">"Bro, let\'s fix your SQL."</div>', unsafe_allow_html=True)

# Conditional Input Based on Selected Mode
user_input = ""
if selected_mode in ["Debug SQL", "Explain SQL", "Optimize SQL", "Be Honest Bro"]:
    user_input = st.text_area("Paste your SQL query", height=200, placeholder="SELECT * FROM users JOIN orders ON users.id = orders.user_id WHERE...")
elif selected_mode == "Generate SQL":
    user_input = st.text_input("Describe what you need in plain English", placeholder="Get the monthly total revenue from the products sold...")
elif selected_mode == "Interview Tips":
    user_input = st.text_input("Topic or paste SQL", placeholder="e.g., Subqueries, Joins, Window Functions, Indexes, or paste a query...")

# Action Button
if st.button("Ask BroSQL"):
    # Error Handling: Validate Inputs
    if not user_input.strip():
        st.error("Please enter a SQL query or description first.")
        st.stop()

    # Prompts Engineering (Emojis stripped completely)
    base_system_prompt = """You are BroSQL AI — a Senior Database Engineer mentoring a junior developer.
Be concise, educational, and use simple language.
Structure every response with clear section headers.
Always end with: Interview Tip — one key takeaway for SQL interviews.
Never execute SQL. Never connect to a database."""

    roast_mode_addon = """ROAST MODE ACTIVE: Before your explanation, add ONE short funny Gen Z roast 
about the mistake or request. Keep it playful, never mean. Then add a divider ━━━━━━━━ 
and continue with your full professional response."""

    # Set base system prompt
    system_prompt = base_system_prompt
    if roast_on:
        system_prompt += f"\n\n{roast_mode_addon}"

    # Setup mode specific prompts (Emojis stripped completely)
    if selected_mode == "Debug SQL":
        user_prompt = f"""Debug this SQL query. Identify all syntax and logical errors.
Return: Error found -> Corrected SQL -> Why it was wrong -> Interview Tip
SQL: {user_input}"""

    elif selected_mode == "Explain SQL":
        user_prompt = f"""Explain this SQL in beginner-friendly terms.
Return: What it does -> Key concepts used -> Real-world analogy -> Interview Tip
SQL: {user_input}"""

    elif selected_mode == "Optimize SQL":
        user_prompt = f"""Optimize this SQL query.
Return: Issues found -> Optimized SQL -> Performance gains explained -> Interview Tip
SQL: {user_input}"""

    elif selected_mode == "Generate SQL":
        user_prompt = f"""Generate a SQL query for: {user_input}
Return: SQL Query (in code block) -> Brief explanation -> Interview Tip"""

    elif selected_mode == "Be Honest Bro":
        user_prompt = f"""Roast this SQL query in Gen Z style (one sentence max, playful not mean).
Then give a full professional debug + explanation.
Return: Roast -> ━━━ -> Explanation -> Correct Query -> Interview Tip
SQL: {user_input}"""

    elif selected_mode == "Interview Tips":
        user_prompt = f"""Give 4-5 SQL interview tips for: {user_input}
Return: common mistakes, best practices, why interviewers ask this, sample Q&A"""

    # Call API with loading spinner state
    with st.spinner("BroSQL is thinking..."):
        try:
            response_text = get_gemini_response(api_key, system_prompt, user_prompt)
            st.session_state.response = response_text
        except Exception as e:
            st.error(f"Gemini API error: {str(e)}")
            st.stop()

# Display Response if exists
if st.session_state.response:
    st.markdown("### Response from BroSQL")
    
    # Styled Card containing the response markdown
    with st.container(border=True):
        st.markdown(st.session_state.response)
        
    st.markdown("### Copy full response")
    st.code(st.session_state.response, language=None)
