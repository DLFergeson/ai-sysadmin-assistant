import requests

API_URL = "https://api.connectwise.com/v4_6_release/apis/3.0/service/tickets"
API_KEY = "your_connectwise_api_key"

def create_ticket(subject, description, company="Internal"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "summary": subject,
        "company": {"identifier": company},
        "initialDescription": description
    }
    # response = requests.post(API_URL, json=payload, headers=headers)
    # return response.json()
    return {"status": "success", "ticket_id": 12345}
