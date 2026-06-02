from langchain_community.document_loaders import PyPDFLoader

# Load the PDF file
loader = PyPDFLoader(r"c:\Users\HP\Downloads\Shrikant_lala_ML (2).pdf")
documents = loader.load()

print (f"\n\nNumber of documents loaded: {len(documents)}\n")
# Print the loaded documents
for doc in documents:
    print(doc.page_content)
    print("\n---\n")  # Separator between pages
    print(f"Metadata: {doc.metadata}\n")