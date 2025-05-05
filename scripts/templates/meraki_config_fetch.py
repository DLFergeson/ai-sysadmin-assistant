import requests

API_KEY = 'your_meraki_api_key'
ORG_ID = 'your_org_id'

headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

response = requests.get(f'https://api.meraki.com/api/v1/organizations/{ORG_ID}/networks', headers=headers)
print(response.json())
