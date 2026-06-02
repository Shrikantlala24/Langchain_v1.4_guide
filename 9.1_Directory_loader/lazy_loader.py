from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(
    path=r'D:\WORK FROM HOME\Github 2\Langchain_v1.4_guide\\9.1_Directory_loader\books',
    recursive=True  # Search subdirectories
)


loaded_docs = loader.lazy_load()
for doc in loaded_docs:
    print(doc.metadata)  # Print the first 500 characters of each document
