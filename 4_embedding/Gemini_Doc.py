from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    output_dimensionality=3,
)

# vectors = 

result = model.embed_documents([
    'what is Deep Learning?',
    'what is Machine Learning?',  
    'what is Generative AI?'
]
)

print(len(result))
print(len(result[0]))
print(result)
