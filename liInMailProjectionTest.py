from voxsup.api.client.linkedin import LinkedInClient as Client
account_id = 500735271 # VoxSup Inc
client = Client(context={'account_id': account_id})
enable_requests_logging()

params = {
    'ids': [930516],
    # 'projection': '(results(*(*,subContent(*(*,adUnitV2~:playableStreams)))))',
    'projection': '(results(*(*,sender(*,displayPictureV2~:playableStreams),subContent(*(*,adUnitV2~:playableStreams)))))',
}
response = client.get('adInMailContentsV2', params=params)
response.json()
