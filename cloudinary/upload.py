import cloudinary

FILE_PATH = "/home/joeklonowski/testVideo.mp4"

result = cloudinary.uploader.upload(FILE_PATH, resource_type="video")
