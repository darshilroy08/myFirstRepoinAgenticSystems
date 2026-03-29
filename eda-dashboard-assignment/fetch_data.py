import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("posts.csv", index=False)

print("Data fetched successfully!")