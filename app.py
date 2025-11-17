import streamlit as st
import json
import os
from core.static_analysis import run_static_analysis
from core.formatter import format_code_with_black
from core.ai_review import ai_review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🧠 AI Code Reviewer using Groq")

uploaded_file = st.file_uploader("📁 Upload Python File", type=['py'])

if uploaded_file:
    file_path = f"samples/{uploaded_file.name}"
    os.makedirs("samples", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ File uploaded successfully: {uploaded_file.name}")

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    st.code(code, language="python")

    # Run Static Analysis
    st.subheader("🔍 Static Analysis")
    analysis = run_static_analysis(file_path)
    st.json(analysis)

    # AI Review (Groq)
    st.subheader("🤖 AI Review")
    ai_feedback = ai_review_code(code)
    st.json(ai_feedback)

    # Save report
    if st.button("💾 Save Report"):
        os.makedirs("reports", exist_ok=True)
        report_path = f"reports/{os.path.splitext(uploaded_file.name)[0]}_report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump({"analysis": analysis, "ai_feedback": ai_feedback}, f, indent=4)
        st.success(f"Report saved: {report_path}")
