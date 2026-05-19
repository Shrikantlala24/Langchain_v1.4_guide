import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI    
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------- Model

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
    )


# ---------------------------------------------------- Prompt Template

prompt = PromptTemplate(

    template='{user_input} in a {explanation_style} manner.', 

    input_variables=['user_input', 'explanation_style']
    )



# ---------------------------------------------------- frontend

st.title("Prompt Chain Example")

input = st.text_input('enter the prompt')
style = st.selectbox('select the explanation style',['casual-explanation', 'exact-definition','balanced'])

if st.button('submit'):
    chain = prompt | model

    response = chain.invoke({
        'user_input': input,
        'explanation_style': style
    })

    st.write(response.content)
