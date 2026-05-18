# don't run it unlesss you have the device suitable for it
# size = 1.19GB
# so Run this file considering
# 1. storage
# 2. GPU (if you have one, it will be faster)
# 3. time (it may take a while to load the model and generate embeddings)

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
try:
    emb = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

    query = "what is deep learning?"

    response_vector = emb.embed_query(query)

    print(str(response_vector))
except Exception as e:
    print(f"An error occurred: {e}")