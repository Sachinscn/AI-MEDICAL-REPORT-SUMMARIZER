import streamlit as st

# 1. Page Configuration (Must be first Streamlit command)
st.set_page_config(
    page_title="HealthPulse AI - Medical Summarizer",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State Initialization

if "selected_language" not in st.session_state:
    st.session_state["selected_language"] = "English"
elif st.session_state["selected_language"] not in ("English", "Hindi", "Telugu", "Kannada"):
    st.session_state["selected_language"] = "English"

if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None

if "current_report_id" not in st.session_state:
    st.session_state["current_report_id"] = None

if "history" not in st.session_state:
    st.session_state["history"] = []

if "theme" not in st.session_state:
    st.session_state["theme"] = "Light"

if "notifications" not in st.session_state:
    st.session_state["notifications"] = True

if "translation" not in st.session_state:
    st.session_state["translation"] = None

if "generating_summary" not in st.session_state:
    st.session_state["generating_summary"] = False

# 3. Multi-page Navigation Config
# Define pages referencing the pages/ folder structures
home_page = st.Page("pages/Home.py", title="Home", icon="🏠", default=True)
upload_page = st.Page("pages/Upload_Report.py", title="Upload Report", icon="📤")
summary_page = st.Page("pages/Summary.py", title="Report Summary", icon="📝")
history_page = st.Page("pages/History.py", title="History Logs", icon="📜")
settings_page = st.Page("pages/Settings.py", title="Settings", icon="⚙️")

# Keep every section visible in one top navigation bar.
pg = st.navigation(
    [home_page, upload_page, summary_page, history_page, settings_page],
    position="top",
)

# Run the navigation routing
pg.run()
