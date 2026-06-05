from langchain_community.document_loaders import WebBaseLoader

url = r'https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhfa4hn-a/p/itm9fce39e65bd7e?pid=COMHH8C57Y6W6NZU&lid=LSTCOMHH8C57Y6W6NZUASDOLA&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=1b52574b-e683-41bf-8494-0b9bea0867cb.COMHH8C57Y6W6NZU.SEARCH&ppt=None&ppn=None&ssid=jkv6jkxx1s0000001780412251855&ov_redirect=true'

loader = WebBaseLoader(url)
data = loader.load()

print(data[0].page_content[:500])