from langchain_community.document_loaders import TextLoader

loader = TextLoader("C:\\Users\\HP\\Downloads\\GSOC research\\ml_tech_stack_comprehensive.txt", encoding="utf-8")

docs = loader.load()

print(docs[0].page_content)