import json
import requests


register_upload = {
	"url": "https://api.linkedin.com/v2/assets?action=registerUpload",
	"headers": {'Content-Type': 'application/json',"Authorization": "Bearer <TOKEN>"},
	"request_body": {
  "registerUploadRequest": {
    "owner": "urn:li:company:<company_id>",
    "serviceRelationships":[{"relationshipType":"OWNER","identifier":"urn:li:userGeneratedContent"}],
    "recipes": [
      "urn:li:digitalmediaRecipe:feedshare-video"
    ]
  }
}
	}



#STEP 1 Register upload
print "\n \n \n ------- Step 1 Register upload------"

resp = requests.post(url=register_upload["url"],headers=register_upload["headers"], json=register_upload["request_body"])
json_data = resp.content
#print json_data
data = json.loads(json_data)
print json.dumps(data, indent=4, sort_keys=True)
print "The video asset id is "+ data["value"]["asset"]


print "\n \n \n-------- Step 2 upload url -----"

upload_file = "/Users/pnihalan/Downloads/SampleVideo_640x360_2mb.mp4"
upload_asset = {
	"headers": data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["headers"],
	"url":data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]}
files = {'upload_file': open(upload_file, 'rb')}


import commands
#Creating curl call
curl_call = "curl -v " 
for k,v in data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["headers"].items():
	curl_call = curl_call+" -H '" + k+":"+v +"'"

curl_call =curl_call+ " --upload-file "+upload_file+ " '"+ data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]+"' "
status, output = commands.getstatusoutput(curl_call)
#print output
print "Video uploaded"



#Step 3 Get uploaded asset's status


print "\n \n \n------- step 3 GET Asset status -----"

print "Sleeping to process upload :)"
import time
time.sleep(60)


resp = requests.get(url="https://api.linkedin.com/v2/assets/"+data["value"]["asset"].split(":")[-1],headers=register_upload["headers"])
json_data = resp.content
#print json_data
parsed_data = json.loads(json_data)
print json.dumps(parsed_data, indent=4, sort_keys=True)

print "\n \nYuppie !! The video asset status is "+ parsed_data["recipes"][0]["status"]





