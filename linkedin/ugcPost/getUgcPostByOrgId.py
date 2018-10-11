from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 502977261 # 4C Insights Test Account
client = Client(context={'account_id': account_id})
enable_requests_logging()

client.headers['X-RestLi-Protocol-Version'] = '2.0.0'

params = {
    'q': 'authors',
    'authors': 'List(urn%3Ali%3Aorganization%3A5021850)'
}
response = client.get('ugcPosts', params=params)
response.json()
