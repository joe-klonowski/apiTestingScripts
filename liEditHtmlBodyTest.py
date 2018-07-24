from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
client = Client(context={'account_id': account_id})
enable_requests_logging()

body = {
    "patch": {
        "$set": {
            "htmlBody": "Hi I'm Joe"
        }
    }
}
response = client.post('adInMailContentsV2/1120974', json=body)
response.json()
