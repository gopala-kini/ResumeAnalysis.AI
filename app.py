from dotenv import load_dotenv
load_dotenv()  #activate the local Env Vars

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Create the Front end of page

st.header(":blue[Resume Analysis] Using AI 👔💼📑",divider='green')
st.subheader("Tips for using the application 💡📖💡")

st.sidebar.subheader("Upload the Resume")

resume=st.sidebar.file_uploader(label="Upload your resume",type=['pdf'])

notes=f'''
* ** Upload the Resume** : Please upload your Resume.This is a GenAI Powered Application
* ** Job Description** :Copy paste the Job Description from Job Boards.
* ** Unleash the Power of Gen AI Model** :Click on the button to generate Insights'''
st.write(notes)

#job desc

st.subheader("Enter the Job Description",divider=True)
job_desc=st.text_area(label="Copy Paste Job description",max_chars=10000)
button=st.button(label="Get AI powered Insights")
if button:
    st.markdown(profile(resume=resume,job_desc=job_desc))
