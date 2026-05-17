from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
)

response = chat.invoke('tell me 5 crazy project ideas on FastAPI and langchain as simple pointers, in very short', temperature=1.8)

print(response.content)