# Best for quick and good documnet loading
# for complex visual PDFs



from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader
from sympy import pprint

loader = OpenDataLoaderPDFLoader(
    file_path=r"C:\Users\HP\Downloads\EAadhaar_SAVED (1).pdf",
    format="markdown"  # Better than "text" for preserving structure
)
documents = loader.load()

for doc in documents:
    print(doc.metadata)
    pprint(doc.page_content)