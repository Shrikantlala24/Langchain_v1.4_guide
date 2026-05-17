from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    temperature=1, 
    max_tokens=1000
)

response = chat.invoke('what is Deep learning')

print(response.content)