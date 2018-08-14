from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 502977261 # 4C Insights Test Account
client = Client(context={'account_id': account_id})
enable_requests_logging()

params = { 'q': 'viewer' }
response = client.get('connections', params=params)
response.json()
