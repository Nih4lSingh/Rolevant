import streamlit as st
import tempfile
from extractor import extract_text_pdf
from matcher import match_role,recommend_roles
import json

with open('role_data.json','r') as f:
    data=json.load(f)

st.title("Rolevant")

uploaded_file=st.file_uploader("Upload your Resume",type="pdf")

role=st.selectbox("Select a role (optional)",["None"]+list(data.keys()))

if st.button("Evaluate"):
    if uploaded_file is None:
        st.warning("Please upload your resume before proceeding")
    else:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path=tmp.name
        resume_text=extract_text_pdf(tmp_path)
        if role!="None":
            score,missing_keywords=match_role(resume_text,role)
            st.write(f"Your Resume is a {round(score*100)}% match for {role}")
            if missing_keywords:
                st.write("Companies also Look for:")
                st.write(', '.join(missing_keywords))
        suggested_roles=recommend_roles(resume_text)
        st.write("Roles best suited for you")
        for i in range(5):
            st.metric(suggested_roles[i][1],'')
