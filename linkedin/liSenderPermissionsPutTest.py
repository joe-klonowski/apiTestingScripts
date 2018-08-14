from voxsup.api.client.linkedin import LinkedInClient as Client
ACCOUNT_ID = 502977261 # 4C Insights Test Account
ACCOUNT_URN = "urn:li:sponsoredAccount:" + str(ACCOUNT_ID)
MEMBER_ID = "-bZaJqJQEO" # Noopur
MEMBER_URN = "urn:li:person:" + MEMBER_ID
client = Client(context={'account_id': ACCOUNT_ID})
enable_requests_logging()

body = {
    "account": ACCOUNT_URN,
    "member": MEMBER_URN,
    "state": "REQUESTED",
}

urlString = 'adInMailMemberSenderPermissions/account=' + ACCOUNT_URN + '&member=' + MEMBER_URN
response = client.put(urlString, json=body)
# content = response.json()
# import json
# json.dumps(content)
