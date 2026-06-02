from langchain_docling.loader import DoclingLoader

FILE_PATH = r"C:\Users\HP\Downloads\EAadhaar_SAVED (1).pdf"

loader = DoclingLoader(file_path=FILE_PATH)

documents = loader.load()
print(documents[0].page_content)
