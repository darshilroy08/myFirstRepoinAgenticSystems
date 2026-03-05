import json

# 1. Store a JSON-formatted string representing an API response
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

# 2. Parse the JSON string into Python objects
data = json.loads(api_response)

# 3. Extract and print required fields
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# 4. Check if confidence score is below 0.9
if confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# 5. Create a new Python dictionary for follow-up result
follow_up = {
    "request_id": request_id,
    "processed": True,
    "message": "Response processed successfully"
}

# Convert dictionary to JSON
follow_up_json = json.dumps(follow_up, indent=4)

# 6. Write JSON output to a file
with open("response.json", "w") as file:
    file.write(follow_up_json)

print("\nFollow-up JSON written to response.json")