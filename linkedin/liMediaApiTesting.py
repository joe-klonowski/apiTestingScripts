from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
client = Client(context={'account_id': account_id})
enable_requests_logging()

params = {
    'ids': [1242663,930516],
    'projection': '(results(*(*,subContent(com.linkedin.ads.AdInMailStandardSubContent(*,adUnitV2~:playableStreams)))))'
}

# response = client.get('adInMailContentsV2', params=params)
response = client.get('adInMailContentsV2', params=params)
content = response.json()
import json
json.dumps(content)
