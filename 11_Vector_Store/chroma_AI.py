import os
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from pypdf import PdfReader
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

PDF_URL = "https://arxiv.org/pdf/2203.11171"
LOCAL_PDF = "paper.pdf"

# Download
if not os.path.exists(LOCAL_PDF):
    response = requests.get(PDF_URL, timeout=30)
    with open(LOCAL_PDF, "wb") as f:
        f.write(response.content)

print("Download ✅")

# Load & split
reader = PdfReader(LOCAL_PDF)
text = "\n".join([page.extract_text() for page in reader.pages])
docs = [Document(page_content=text)]

# PyPDFLoader is in use
loader = PyPDFLoader(file_path=LOCAL_PDF, images_inner_format="markdown-img")
docs_2 = loader.load()
print("✅ PyPDFloaded")
# -------------------------------------------------------

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# splitting the docs_2 into chunks_2
chunks_2 = splitter.split_documents(docs_2)

print("load & split ✅")

# Embed & store

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    chunks, embeddings, persist_directory="./chroma_db", collection_name="arxiv_paper"
)

vectorstore_2 = Chroma.from_documents(
    chunks_2,
    embeddings,
    persist_directory="./chroma_db_2",
    collection_name="arxiv_paper",
)

print("embed & store ✅")

# Retrieve
retriever = vectorstore_2.as_retriever(
    search_type="mmr", search_kwargs={"k": 5, "lambda_mult": 0.5}
)
results = retriever.invoke("results")

print("retrieve ✅")

for i, doc in enumerate(results, 1):
    print(f"\n--- {i} ---\n{doc.page_content[:500]}")
