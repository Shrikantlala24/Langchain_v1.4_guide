from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(
    path=r'D:\WORK FROM HOME\Github 2\Langchain_v1.4_guide\\9.1_Directory_loader\books',
    recursive=True  # Search subdirectories
)

loaded_docs = loader.load()
print(len(loaded_docs))
print(loaded_docs[0].page_content[:500])  # Print the first 500 characters of the first document

# An Introduction to Probability and Statistics
# (statistics 325)
# J. Calvin Berry
# Mathematics Department
# University of Louisiana at Lafayette
# https://www.ucs.louisiana.edu/ ~ jcb0773/
# July 2025 revision
# c⃝ 2017, 2022, 2024, 2025 J. Calvin Berry
# 20250721