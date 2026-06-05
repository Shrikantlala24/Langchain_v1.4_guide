from langchain_community.document_loaders import PlaywrightURLLoader

urls = [
    "https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhfa4hn-a/p/itm9fce39e65bd7e"
]

loader = PlaywrightURLLoader(
    urls=urls,
    remove_selectors=["script", "style"]
)

docs = loader.load()

print(docs[0].page_content[:1000])