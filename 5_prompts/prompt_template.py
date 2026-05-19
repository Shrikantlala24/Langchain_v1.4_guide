import streamlit as st

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)


st.title("Google Generative AI Prompt Template")
user_input = st.text_input("Enter your prompt here:")

if st.button("Generate Response"):
    if user_input:
        
        response = llm.invoke(user_input)

        st.write("Generated Response:")
        st.write(response)
    else:
        st.warning("Please enter a prompt to generate a response.")


# if 
