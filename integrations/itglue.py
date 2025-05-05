import requests

API_URL = "https://api.itglue.com"
API_KEY = "your_itglue_api_key"

def search_docs(keyword):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/vnd.api+json"
    }
    params = {"filter[name]": keyword}
    # response = requests.get(f"{API_URL}/documents", headers=headers, params=params)
    # return response.json()
    return [f"Mock doc match for '{keyword}'"]
