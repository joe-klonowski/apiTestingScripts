from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
COMPANY_ID = 3026918 # VoxSup Inc
INMAIL_ID = 1225113 # Testing preview
client = Client(context={'account_id': account_id})
enable_requests_logging()

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
      "urn:li:digitalmediaRecipe:spinmail-banner-image"
    ]
  }
}
registerHeaders = {
  "Content-Type": "application/json"
}

registerResponse = client.post('assets', params=registerParams, json=registerBody, headers=registerHeaders)
content = registerResponse.json()
import json
json.dumps(content)

uploadRequestFromLI = content['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']
headers = uploadRequestFromLI['headers']
uploadUrl = uploadRequestFromLI['uploadUrl']
asset = content['value']['asset']
assetId = trimMediaAssetURN(asset)

print('headers: ' + json.dumps(headers))
print('uploadUrl: ' + json.dumps(uploadUrl))
print('assetId: ' + assetId)

uploadHeaders = {
  # 'Content-Type': 'image/png',
  # 'Content-Length': '189435'
}
files = {'file': ("image.png", open('/home/joeklonowski/voxsupFrontend2/image.png', 'rb'), 'image/png')}
uploadResponse = client.put(uploadUrl, files=files, headers=uploadHeaders)

getResponse = client.get('assets/' + assetId)
getResponse.json()

# updateBody = {
#   "patch": {
#     "$set": {
#       "subContent": {
#         "com.linkedin.ads.AdInMailStandardSubContent": {
#           "actionText": "HMC",
#           "action": "https://www.hmc.edu/",
#           "adUnitV2": asset
#         }
#       }
#     }
#   }
# }
# updateResponse = client.post('adInMailContentsV2/' + str(INMAIL_ID), json=updateBody)
# updateResponse.json()

# getInMailParams = {
#   'projection': '(id,subContent(com.linkedin.ads.AdInMailStandardSubContent(adUnitV2~:playableStreams)))'
# }
# getInMailResponse = client.get('adInMailContentsV2/' + str(INMAIL_ID), params=getInMailParams)
# getInMailResponse.json()
