import http.client

conn = http.client.HTTPConnection("ejv5qn.api.infobip.com")
payload = ''
headers = {
    'Authorization': '{authorization}',
    'Accept': 'application/json'
}
conn.request("GET", "/sms/1/reports?limit=null&applicationId=marketing-automation-application&entityId=promotional-traffic-entity", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
