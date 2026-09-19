from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=1,
    # max_tokens=1000
)

response = chat.invoke("what is Deep learning")

print(response.content)
