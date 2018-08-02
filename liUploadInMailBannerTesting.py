from voxsup.api.client.linkedin import LinkedInClient as Client
from requests import Request, Session

account_id = 500735271 # VoxSup Inc
COMPANY_ID = 3026918 # VoxSup Inc
INMAIL_ID = 1225113 # Testing preview
AUTH_TOKEN = 'AQUpNzFf2yuWxcy82SyzphIC2LCSPzLwMMnr08PrU1Gkcp5k7v0hQj_TF04z9AdIVsAd4dHV7GUaRnBdkMla747STTEtbMDDHixJYjJrFHxsNpv3EmJ8XV3OnDPtJWwO3N7k7SR-dN0UnEpVdwRjrojZIj1W6Sz_W6Bz1Ooyl764PrIakPPV9OklNBXQ0GrsttIkjU8smvG6_79VgtQeCv53CY7lhY1E1QnXjjt2d_gTpMkkWAF5QZWnO8ccSHjNgVYAf8_512swlaPN8dWBw5gOXWA5eNUHAdOSZDixYqLth_59oZoNAwXsWTmA8fMAOKhxFcpO_ltPqOBlHXtIfcSgKvu4lQ'
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


files = {'file': ("image.png", open('/home/joeklonowski/voxsupFrontend2/image.png', 'rb'), 'image/png')}
uploadRequest = Request('PUT', uploadUrl, files=files)
preppedRequest = uploadRequest.prepare()
del preppedRequest.headers['Content-Type']
# del preppedRequest.headers['Content-Length']
preppedRequest.headers['Authorization'] = 'Bearer ' + AUTH_TOKEN
uploadResponse = client.send(preppedRequest)

# uploadHeaders = {
#   'Content-Type': None,
#   # 'Content-Length': '189435'
# }
# uploadResponse = client.put(uploadUrl, files=files, headers=uploadHeaders)

getHeaders = {
  'Cache-Control': 'no-cache'
}
getResponse = client.get('assets/' + assetId, headers=getHeaders)
json.dumps(getResponse.content)

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
