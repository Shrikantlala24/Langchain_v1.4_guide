# for tabular content in PDF

from langchain_community.document_loaders import PDFPlumberLoader
from pprint import pprint

loader = PDFPlumberLoader("C:\\Users\\HP\Downloads\\resume - ayush jadia.pdf")

data = loader.load()

pprint(data[1].page_content)