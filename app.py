import streamlit as st
from core import ai_engine, db_manager, calendar_sync
from utils import pdf_gen, mailer, i18n_utils

st.set_page_config(layout="wide")
lang = st.sidebar.selectbox("Language", ["Japanese", "English"])
_ = i18n_utils.get_translator(lang)

st.title("⚡ AI Enterprise Platform")

if st.sidebar.button(_("Sync Calendar")):
    st.session_state.memo = calendar_sync.get_today_events()

memo = st.text_area("Input Memo", value=st.session_state.get("memo", ""))

if st.button(_("Generate")):
    report = ai_engine.generate_report(memo)
    db_manager.save_report(report)
    st.session_state.report = report

if "report" in st.session_state:
    st.write(st.session_state.report)
    if st.button(_("Download PDF")):
        path = pdf_gen.PDFGenerator("Report").create(st.session_state.report)
        with open(path, "rb") as f:
            st.download_button("File", f, "report.pdf")