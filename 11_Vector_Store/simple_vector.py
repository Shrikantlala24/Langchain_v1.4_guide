from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# from langchain_community.retrievers import

load_dotenv()

docs = [
    Document(
        page_content="Langchain is the best library for building LLM powered apps"
    ),
    Document(page_content="LLM powered apps are build using Langchain library"),
    Document(
        page_content="LLM orchestration is the key for Building any AI-powered services"
    ),
    Document(
        page_content="Agentic AI is the new buzz word in the service based companies"
    ),
    Document(
        page_content="is it not obvious that AI can replace you if you are doing something replacable?"
    ),
    Document(
        page_content="AI is not good at experiential thinking, it only generates text even using langchain"
    ),
    Document(
        page_content="LLMs are just helping with the text generation and Natural language understanding, the System build around it are making them extraordinary"
    ),
]

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", output_dimensionality=36
)

vector_store = FAISS.from_documents(embedding=embedding_model, documents=docs)

# Configure a vector store as an MMR retriever
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,  # Total number of documents to retur
        # Number of documents to fetch before MMR re-ranking
        "lambda_mult": 1,  # Diversity factor (0 = max diversity, 1 = max relevance)
    },
)

# Use the retriever in your RAG pipeline
query = retriever.invoke("langchain")

print(query)
