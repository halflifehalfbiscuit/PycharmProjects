import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\":\t{\n\t\t\"attributes\" : {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}\n\t\t"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY29hcGlj"
    }

response = requests.request("POST", url, data=payload, headers=headers)
json_response =  json.loads(response.text)

print(response.text)
tokenfromlogin = (json_response['imdata'] [0]['aaaLogin']['attributes']['token'])


url = "http://192.168.10.1/api/node/mo/uni/tn-great_tenant.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-great_tenant\",\"name\":\"great_tenant\",\"rn\":\"tn-great_tenant\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-cookie": tokenfromlogin}
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)
