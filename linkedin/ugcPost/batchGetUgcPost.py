from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 502977261 # 4C Insights Test Account
client = Client(context={'account_id': account_id})
enable_requests_logging()

client.headers['X-RestLi-Protocol-Version'] = '2.0.0'

params = 'ids=List(urn%3Ali%3AugcPost%3A6456174447488430082,urn%3Ali%3AugcPost%3A6452598395432505344)'
response = client.get('ugcPosts?' + params)
response.json()
