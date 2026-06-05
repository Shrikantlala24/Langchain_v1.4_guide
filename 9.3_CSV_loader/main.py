from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"C:\Users\HP\Downloads\placement.csv")

docs = loader.load()

print(docs[0].page_content[:1000])