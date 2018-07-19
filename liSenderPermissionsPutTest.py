from voxsup.api.client.linkedin import LinkedInClient as Client
ACCOUNT_ID = 500735271 # VoxSup Inc
ACCOUNT_URN = "urn:li:sponsoredAccount:" + str(ACCOUNT_ID)
COMPANY_ID = 3026918 # VoxSup Inc
MEMBER_ID = "YvvwSuc8fR" # Salo
MEMBER_URN = "urn:li:person:" + MEMBER_ID
client = Client(context={'account_id': ACCOUNT_ID})
enable_requests_logging()

params = {
    "account": ACCOUNT_URN,
    "member": MEMBER_URN,
}

body = {
    "account": ACCOUNT_URN,
    "member": MEMBER_URN,
    "state": "REQUESTED",
}

# response = client.put('adInMailMemberSenderPermissions', params=params, json=body)
urlString = 'adInMailMemberSenderPermissions/account=' + ACCOUNT_URN + '&member=' + MEMBER_URN
response = client.put(urlString, json=body)
content = response.json()
import json
json.dumps(content)
