from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(
    path=r'D:\WORK FROM HOME\Github 2\Langchain_v1.4_guide\9_1_Directory_loader\books',
    recursive=True  # Search subdirectories
)


loaded_docs = loader.lazy_load()
print(len(loaded_docs))
print(loaded_docs[0].page_content[:500])  # Print the first 500 characters of the first document
