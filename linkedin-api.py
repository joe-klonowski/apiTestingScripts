from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 502977261 # 4C Insights Test Account
client = Client(context={'account_id': account_id})
enable_requests_logging()

# client.headers['X-RestLi-Protocol-Version'] = '2.0.0'

# response = client.get('people/id=1LGB3s99Xm')
params = { 'ids': 'List((id:Fly49JJXMn),(id:1LGB3s99Xm),(id:rOCE-Baqcl))' }
response = client.get('people', params=params)
# response.json()
