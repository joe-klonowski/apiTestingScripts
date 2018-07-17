from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
COMPANY_ID = 3026918 # VoxSup Inc
client = Client(context={'account_id': account_id})
enable_requests_logging()

params = {
    'action': 'registerUpload',
}
body = {
  "registerUploadRequest": {
    "owner": "urn:li:company:" + str(COMPANY_ID),
    "serviceRelationships":[{"relationshipType":"OWNER","identifier":"urn:li:userGeneratedContent"}],
    "recipes": [
      "urn:li:digitalmediaRecipe:spinmail-banner-image"
    ]
  }
}

registerResponse = client.post('assets', params=params, json=body)
content = registerResponse.json()
import json
json.dumps(content)

uploadRequest = content['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']
headers = uploadRequest['headers']
uploadUrl = uploadRequest['uploadUrl']

print('headers: ' + json.dumps(headers))
print('uploadUrl: ' + json.dumps(uploadUrl))
