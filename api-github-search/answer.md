# Conceptual Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to send extra information to the API through the URL.  
In this request, query parameters help define:

- `q=python` → searches repositories related to Python
- `sort=stars` → sorts repositories by number of stars
- `order=desc` → arranges results in descending order
- `per_page=5` → limits output to 5 repositories

So, query parameters control what data we want and how the API should return it.

## 2. Why do we use `response.json()` instead of `response.text`?

We use `response.json()` because the GitHub API returns data in JSON format.  
`response.json()` converts that JSON data directly into a Python dictionary, which makes it easy to access values like repository name and stars.

`response.text` only gives the raw response as plain text, which is harder to work with when extracting specific data.