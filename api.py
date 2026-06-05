import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "2fb2e42f5573bffd1c1ab26478f1edc"
BASE_URL = "https://api.themoviedb.org/3"

response = requests.get(
    url=f"{BASE_URL}/movie/popular",
    params={
        "api_key": API_KEY,
        "language": "en-US",
        "page": 1
    },
    verify=False  # ← ADD THIS
)

if response.status_code == 200:
    data = response.json()
    movies = data["results"]
    for movie in movies:
        print(movie["title"], "| Rating:", movie["vote_average"])
else:
    print(f"Error {response.status_code}: {response.text}")

# After your requests.get call

# Save the HTML response to a file
with open("response.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved to response.html")