import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE-GEMINI-API-KEY"))
model=genai.GenerativeModel('gemini-2.0-flash')

# Read the pdf
def profile(resume,job_desc):
    if resume is not None:
        resume_doc=read_pdf(resume)
        st.markdown("Resume has been Uploaded")
    else:
        st.warning("Resume Missing")
    response=model.generate_content(f'''Act as a HR or OPs head in AI domain and compare {resume} with {job_desc}and suggest= what are the chances of getting selected?''')
    #Return the result
    return(st.write(response.text))
    