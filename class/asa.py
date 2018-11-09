import requests

url = "https://192.168.10.100/api/interfaces/physical"

payload = "{\n  \"ned:Loopback\": {\n    \"name\": 200,\n    \"ip\": {\n      \"address\": {\n        \"primary\": {\n          \"address\": \"160.99.1.1\",\n          \"mask\": \"255.255.255.0\"\n        }\n      }\n    }\n  }\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("GET", url, verify=False, data=payload, headers=headers)

print(response.text)
