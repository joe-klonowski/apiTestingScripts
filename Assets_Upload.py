import json
import requests

account_id = 500735271 # VoxSup Inc
COMPANY_ID = 3026918 # VoxSup Inc
INMAIL_ID = 1225113 # Testing preview
AUTH_TOKEN = 'AQWXKBmSvxt40kGcvg92Jn-1QUIyXczXmrzMayteVOeQ3a5eFfqJH746_TInOgmTMrhbwSDIKDZX0-tT4CUVFCx3okfXSoICslJaI3srNy9Xit2nH7DBuXz_yB09Lmj6QSwjv0sXea87Wtq7dcztfFgdSpcAYQIXp9rmxQx9dNWa2RhHf4wqeFxAmoUXZF5UfGPlqrcynp0d3z-Zn1eGlqC7TxElBy3kns0J0L92ztbH0-8KVxm0xloCbGmaawG9wUXBEfLn0Z5N0GBzXmICP-C3XYAgnIMLAPOMtIbKksPd2aGLEFzwfVjtXf6EHdxj5QlXNh3cDW7GjH_xDu49eF7G_Y_trw'
FILE_PATH = '/home/joeklonowski/voxsupFrontend2/image.png'

register_upload = {
	"url": "https://api.linkedin.com/v2/assets?action=registerUpload",
	"headers": {'Content-Type': 'application/json',"Authorization": "Bearer " + AUTH_TOKEN},
	"request_body": {
      "registerUploadRequest": {
        "owner": "urn:li:company:" + str(COMPANY_ID),
        "serviceRelationships":[{"relationshipType":"OWNER","identifier":"urn:li:userGeneratedContent"}],
        "recipes": [
            "urn:li:digitalmediaRecipe:spinmail-banner-image"
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

upload_asset = {
	"headers": data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["headers"],
	"url":data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]}
files = {'upload_file': open(FILE_PATH, 'rb')}


import commands
#Creating curl call
curl_call = "curl -v "
for k,v in data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["headers"].items():
	curl_call = curl_call+" -H '" + k+":"+v +"'"

curl_call =curl_call+ " --upload-file "+FILE_PATH+ " '"+ data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]+"' "
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





