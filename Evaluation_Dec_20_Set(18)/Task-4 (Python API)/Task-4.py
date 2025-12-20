import requests


api_url = "https://reqres.in/api/users"
headers = {
    "Authorization": "Bearer reqres-token",
    "Content-Type": "application/json"
}
payload = {
    "name": "smith",
    "job": "agent"
}

response = requests.post(api_url, json=payload, headers=headers)
response_data = response.json()
status_code = response.status_code
print("Response Data:", response_data)

input_name = payload["name"]
received_name = response_data.get("name")

print (f" user '{received_name}' created matches input.")