from markitdown import MarkItDown

md = MarkItDown()
result = md.convert(r"C:\Users\HP\Downloads\1000195595.png")
print(result.text_content)