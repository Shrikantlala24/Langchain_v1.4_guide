import streamlit as st

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
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



if user_input:

    explanation_style = st.selectbox("Select Explanation style", ["beginner-friendly", "detailed", "concise"])
    length = st.selectbox("Select response length", ["short", "medium", "long"])

    if st.button('Generate Response with Template'):
        
        template = PromptTemplate(
        input_variables=["user_input", "explanation_style", "length"],
        template="{user_input} in a {explanation_style} manner and keep the response {length}."
        )

        final_prompt = template.invoke({
                "user_input": user_input, "explanation_style": explanation_style, "length": length
                })
        response = llm.invoke(final_prompt)
        st.write("Generated Response with Template:")
        st.write(response)
    else:
        st.warning("Please enter a prompt to generate a response.")
