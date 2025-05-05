# Check HPE iLO health using Redfish API
import requests

url = "https://ilo-host/redfish/v1/Systems/1/"
auth = ('admin', 'your_password')
response = requests.get(url, verify=False, auth=auth)
print(response.json())
