from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(
    path=r'D:\WORK FROM HOME\Github 2\Langchain_v1.4_guide\9_1_Directory_loader\books',
    recursive=True  # Search subdirectories
)

loaded_docs = loader.load()
print(len(loaded_docs))