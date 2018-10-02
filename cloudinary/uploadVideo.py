from voxsup.cloudinary.client import Client as CloudinaryClient

FILE_PATH = "/home/joeklonowski/testVideo.mp4"

cloudinaryClient = CloudinaryClient()
result = cloudinaryClient.uploader.upload(FILE_PATH, resource_type="video")
