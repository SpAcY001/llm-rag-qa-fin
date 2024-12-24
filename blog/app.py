import streamlit as st
from langchain.llms import ctransformers
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="LangChain", page_icon="🔗", layout="centered", initial_sidebar_state="collapsed")
st.head("generate blog")
input_text = st.text_input("Enter your blog topic here", height=200)

col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input('No. of words')
with col2:
    blog_style = st.selectbox('Select blog style', ['formal', 'informal', 'casual', 'technical'])