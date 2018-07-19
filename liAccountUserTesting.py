from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
COMPANY_ID = 3026918 # VoxSup Inc
client = Client(context={'account_id': account_id})
enable_requests_logging()

params = {
    'q': 'accounts',
    'accounts': 'urn:li:sponsoredAccount:500735271',
    'projection': '(elements*(user~))',
}

response = client.get('adAccountUsersV2', params=params)
content = response.json()
import json
json.dumps(content)
