import streamlit as st

from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def response():
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

    response = model("what are components of Machine learning. tell me in short under 100 words.")

    return response

perm_response = response()
print(perm_response)



if st.button("Generate Response"):
    st.write(perm_response)
