from langchain_huggingface import ChatHuggingFace ,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm_info = HuggingFacePipeline(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text_generation',
    model_kwargs={"temperature": 1, "max_length": 1000}
)

model = ChatHuggingFace(llm=llm_info)

response = model.invoke('What is Deep learning?')
print(response.content)