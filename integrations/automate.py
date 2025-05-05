import requests

API_URL = "https://automate.yourdomain.com/api"
API_KEY = "your_automate_api_key"

def trigger_script_on_agent(agent_id, script_name):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "agent_id": agent_id,
        "script": script_name
    }
    # response = requests.post(f"{API_URL}/run-script", json=payload, headers=headers)
    # return response.json()
    return {"agent_id": agent_id, "script": script_name, "status": "dispatched"}
