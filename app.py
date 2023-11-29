#RecursiveCharacterTextSplitter: chunksize 500, OpenAIEmbeddings & OpenAI LLM

import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import json  # 导入json模块

st.set_page_config(page_title="USinoIP Website AI Chat Assistant", layout="wide")
st.subheader("Welcome to USinoIP Website AI Chat Assistant.")
st.write("Important notice: This USinoIP Website AI Chat Assistant is offered ONLY for the purpose of assisting users to better interact with USinoIP webiste contents and by no means for any other use. Any user should never interact with the AI Assistant in any way that is against any related promulgated regulations. The user is the only entity responsible for interactions taken between the user and the AI Chat Assistant.")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def call_chatbot_api(query):    
    url = 'https://binqiangliu-usinositeopenaillmchunksize500fastapi.hf.space/api/chat'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"
    }    
    json_data_for_api = {'user_question': query}
    
    #response = requests.post(url, json=json_data_for_api) 
    #response = requests.post(url, headers=headers, json=json_data_for_api)   #This format is working
    
    #response = requests.post(url, headers=headers, data=json.dumps(data))    #NameError: name 'json' is not defined
    response = requests.post(url, headers=headers, data=json.dumps(json_data_for_api))   #This format needs 'import json', or else NameError: name 'json' is not defined
    
    result = response.json()
    return result['response']
    
user_query = st.text_input("Enter your query here:")

if st.button('Get AI Response'):
    with st.spinner("AI Thinking...Please wait a while to Cheers!"):    
        if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
            response = call_chatbot_api(user_query)
            st.write("USino AI Response:")
            st.write(response)
        print(response)  # 打印Chatbot的响应
