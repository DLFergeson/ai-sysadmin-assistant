import requests

API_URL = "https://auvikapi.com/v1"
API_KEY = "your_auvik_api_key"

def get_device_status(device_name):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    # response = requests.get(f"{API_URL}/devices?filter[name]={device_name}", headers=headers)
    # return response.json()
    return {"device_name": device_name, "status": "online", "uptime": "72h"}
