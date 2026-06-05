from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(r"C:\Users\HP\Downloads\Shrikant_lala_ML (2).pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)