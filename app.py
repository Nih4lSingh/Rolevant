import streamlit as st
import tempfile
from extractor import extract_text_pdf
from matcher import match_role,recommend_roles
import json

with open('role_data.json','r') as f:
    data=json.load(f)
st.title("Rolevant")
uploaded_file=st.file_uploader("**Upload your Resume**",type="pdf")
role=st.selectbox("**Select a role (optional)**",["None"]+list(data.keys()))

def colored_progress_bar(percent):
    if percent > 65:
        color = "#4ade80"  # green
    elif percent > 50:
        color = "#3b82f6"  # blue
    else:
        color = "#9ca3af"  # gray
    st.markdown(f"""
        <div style="background-color:#1f2937; border-radius:8px; height:14px; width:100%;">
            <div style="background-color:{color}; width:{percent}%; height:100%; border-radius:8px;"></div>
        </div>
    """, unsafe_allow_html=True)

if st.button("**Evaluate**"):
    if uploaded_file is None:
        st.warning("**Please upload your resume before proceeding**")
    else:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path=tmp.name
        resume_text=extract_text_pdf(tmp_path)       
        if role!="None":
            score,missing_keywords=match_role(resume_text,role)
            col1, col2 = st.columns(2)
            with col1:
                score=max(0, min(100, round((score-0.3)/(0.45) * 100)))
                if score>65:
                    st.metric("**Match Score**", f"**:green[{score}%]**")
                elif score>50:
                    st.metric("**Match Score**", f"**:blue[{score}%]**")
                else:
                    st.metric("**Match Score**", f"**:gray[{score}%]**")
                colored_progress_bar(score)
            st.divider()
            with col2:
                if len(missing_keywords)>0:
                    st.write("**Companies also look for:**")
                    missing_keywords=list(set(missing_keywords))
                    top_skills=missing_keywords[:10]
                    remaining_skills=missing_keywords[10:]
                    if len(top_skills)>0:
                        st.markdown(
                            " ".join([f"<span style='background-color:#1f2937;color:#FFFFFF;padding:4px 10px;border-radius:12px;margin:2px;display:inline-block;font-size:14px'>{s}</span>" for s in top_skills]),
                            unsafe_allow_html=True
                            )
                    if remaining_skills:
                        with st.expander(f"+{len(remaining_skills)} more skills"):
                            remaining_badges = " ".join([f"<span style='background-color:#1f2937;color:#FFFFFF;padding:4px 10px;border-radius:12px;margin:2px;display:inline-block;font-size:14px'>{s}</span>" for s in remaining_skills])
                            st.markdown(remaining_badges, unsafe_allow_html=True)
                
        suggested_roles=recommend_roles(resume_text)
        st.write("**Recommended Roles Based on Your Resume:**")
        for i in range(5):
            cola, colb, colc = st.columns(3)
            score=max(0, min(100, round((suggested_roles[i][0]-0.3)/(0.45) * 100)))
            with cola:
                st.markdown(f"**{suggested_roles[i][1]}**")
            with colb:
                colored_progress_bar(score)
            with colc:
                if score>65:
                    st.markdown(f":green[{score}%] match")
                elif score>50:
                    st.markdown(f":blue[{score}%] match")
                else:
                    st.markdown(f":gray[{score}%] match")