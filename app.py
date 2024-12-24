from langchain.llms import OpenAI
from langchain.chat_models.azure_openai import AzureChatOpenAI
import os
import streamlit as st

# function to load openai model and get response
os.environ["OPENAI_API_TYPE"] = "azure"
 
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"
 
os.environ["AZURE_OPENAI_API_KEY"] = "611dff392d7a4f3780f84060b3d6bc9e"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://openai-nonfunsbx-pprd-01.openai.azure.com/openai/deployments/gpt-4-finance/chat/completions?api-version=2023-07-01-preview"

def get_openai_response(question):
    llm = AzureChatOpenAI(
    openai_api_version="2023-07-01-preview",
    azure_deployment="gpt-4",
    model_version="gpt-4"
    )
    response = llm.predict(question)
    return response

st.set_page_config(page_title="OpenAI Chatbot", page_icon=":robot:")
st.header("OpenAI Chatbot")

input=st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Submit")

if submit:
    st.subheader("The response is")
    st.write(response)

