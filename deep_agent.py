from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_vercel_sandbox import VercelSandbox
from vercel.sandbox import Sandbox

from dotenv import load_dotenv

load_dotenv()

# Create sandbox
sandbox = Sandbox.create()  # or Sandbox() depending on the API
backend = VercelSandbox(sandbox=sandbox)

agent = create_deep_agent(
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    # Delete sandbox - use the correct method
    sandbox.delete()  # OR: sandbox.close() - check VercelSandbox API