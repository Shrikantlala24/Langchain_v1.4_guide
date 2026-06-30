# os for file checking
# requests for getting PDF

import os
import requests

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv

load_dotenv()


PDF_URL = "https://arxiv.org/pdf/2605.20275"
LOCAL_FILE = "paper.pdf"

# Donwload
if not os.path.exists(LOCAL_FILE):
    response = requests.get(PDF_URL)
    with open(LOCAL_FILE, 'wb') as file :
        file.write(response.content)
        print(response)

