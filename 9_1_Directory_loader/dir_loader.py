from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='D:\WORK FROM HOME\Github 2\Langchain_v1.4_guide\9_1_Directory_loader\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

loaded_docs = loader.load()
print(len(loaded_docs))

# It's not working, try PyPDFDirectoryLoader instead of DirectoryLoader with PyPDFLoader