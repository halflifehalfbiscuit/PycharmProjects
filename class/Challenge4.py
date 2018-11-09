#   Note that this script expects HTTP port 80 on the APIC, which is off by default.
# 	To enable HTTP in the APIC, navigate to FABRIC, FABRIC POLICIES Pod Policies     Policies   Management Acces    default  then enable HTTP
import requests
import json

def get_cookies(apic):
    username = 'admin'
    password = 'ciscoapic'
    url = apic + '/api/aaaLogin.json'
    auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies

def add_tenant(apic,cookies):
    jsondata = {"fvTenant":{"attributes":{"dn":"uni/tn-acme","name":"acme","rn":"tn-acme","status":"created"},"children":[]}}
    result = requests.post('{0}://{1}/api/node/mo/uni/tn-acme.json'.format(protocol,host), cookies=cookies, data=json.dumps(jsondata), verify=False)
    print result.status_code
    print result.text

def get_tenants(apic,cookies):
    uri = '/api/class/fvTenant.json'
    url = apic + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response

def add_application_profile(apic,cookies):
    jsondata = {"fvAp":{"attributes":{"dn":"uni/tn-acme/ap-Accounting","name":"Accounting","rn":"ap-Accounting","status":"created"},"children":[]}}
    result = requests.post("{0}://{1}/api/node/mo/uni/tn-acme/ap-Accounting.json".format(protocol, host), cookies=cookies, data=json.dumps(jsondata), verify=False)
    print result.status_code
    print result.text

def add_EPG1(apic,cookies):
    jsondata = {"fvAEPg":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Payroll","name":"Payroll","rn":"epg-Payroll","status":"created"},"children":[{"fvCrtrn":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Payroll/crtrn","name":"default","rn":"crtrn","status":"created,modified"},"children":[]}}]}}
    result = requests.post("{0}://{1}/api/node/mo/uni/tn-acme/ap-Accounting/epg-Payroll.json".format(protocol, host), cookies=cookies, data=json.dumps(jsondata), verify=False)
    print result.status_code
    print result.text

def add_EPG2(apic,cookies):
    jsondata = {"fvAEPg":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Bills","name":"Bills","rn":"epg-Bills","status":"created"},"children":[{"fvCrtrn":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Bills/crtrn","name":"default","rn":"crtrn","status":"created,modified"},"children":[]}}]}}
    result = requests.post("{0}://{1}/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json".format(protocol, host), cookies=cookies, data=json.dumps(jsondata), verify=False)
    print result.status_code
    print result.text

if __name__ == "__main__":
    protocol = 'http'
    host = '192.168.10.1'
    apic = '{0}://{1}'.format(protocol, host)
    cookies = get_cookies(apic)
    add_tenant(apic,cookies)
    add_application_profile(apic,cookies)
    add_EPG1(apic,cookies)
    add_EPG2(apic,cookies)
    rsp = get_tenants(apic,cookies)

rsp_dict = json.loads(rsp)
tenants = rsp_dict['imdata']

for tenant in tenants:
    print tenant['fvTenant']['attributes']['name']
