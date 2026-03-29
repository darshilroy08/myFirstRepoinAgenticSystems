import os
import requests

# 1. Retrieve API key from environment variable
api_key = os.getenv("API_KEY")

if not api_key:
    print("Error: API_KEY not found in environment variables")
    exit()

# 2. Send GET request to given endpoint
url = "https://api.example.com/data"

# 3. Include API key in Authorization Bearer format
headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers)

    # 4. Handle status codes
    if response.status_code == 200:
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)