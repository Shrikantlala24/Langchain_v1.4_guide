from pprint import pprint
from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

    

llm_info = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text_generation'
)

model = ChatHuggingFace(llm=llm_info)

prompt_1 = PromptTemplate(
    template = 'explain this topic : {topic}',
    input_variables = ['topic']
)

prompt_2 = PromptTemplate(
    template = 'Now explain this topic in a very simple way in 3 lines: {topic}',
    input_variables = ['topic']
)

parser  = StrOutputParser()



chain = prompt_1 | model | parser 
chain2 =  chain | prompt_2 | model | parser

response = chain.invoke({'topic': 'Deep learning'})
pprint(response)
response2 = chain2.invoke({'topic': 'Deep learning'})
pprint(response2)