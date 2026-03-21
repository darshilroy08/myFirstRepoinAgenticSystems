import requests

# API endpoint
url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}

# Send GET request
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    print("Top 5 Python repositories on GitHub:\n")

    for repo in data["items"]:
        print(f"Repository Name: {repo['full_name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print("-" * 40)
else:
    print("Error:", response.status_code)
    print(response.text)