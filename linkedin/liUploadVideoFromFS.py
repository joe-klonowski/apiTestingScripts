from voxsup.api.client.linkedin import LinkedInClient as Client
import requests

account_id = 502977261 # 4C Insights Test Account
COMPANY_ID = 5021850 # 4C Insights
client = Client(context={'account_id': account_id})
# enable_requests_logging()

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def trimMediaAssetURN(urn):
  return remove_prefix(urn, 'urn:li:digitalmediaAsset:')

registerParams = {
    'action': 'registerUpload',
}
registerBody = {
  "registerUploadRequest": {
    "owner": "urn:li:company:" + str(COMPANY_ID),
    "serviceRelationships":[{"relationshipType":"OWNER","identifier":"urn:li:userGeneratedContent"}],
    "recipes": [
      "urn:li:digitalmediaRecipe:ads-video"
    ]
  }
}

registerResponse = client.post('assets', params=registerParams, json=registerBody)
content = registerResponse.json()
import json
json.dumps(content)

uploadRequestFromLI = content['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']
assetUploadHeaders = uploadRequestFromLI['headers']
assetUploadUrl = uploadRequestFromLI['uploadUrl']
asset = content['value']['asset']
assetId = trimMediaAssetURN(asset)

print('headers: ' + json.dumps(assetUploadHeaders))
print('uploadUrl: ' + json.dumps(assetUploadUrl))
print('assetId: ' + assetId)

with open('/home/joeklonowski/testVideo.mp4', 'rb') as data:
  requests.put(assetUploadUrl, data, headers=assetUploadHeaders)

getResponse = client.get('assets/' + assetId)
getResponse.json()
