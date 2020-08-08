import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = "geetechlab-com",
    api_key = "622236724885358",
    api_secret = "ZqOEAuVc4BLHp1bMkhxKJ51ye2s"
)

cloudinary_url = "https://api.cloudinary.com/v1_1/geetechlab-com"
cloudinary_upload_preset = "r3fz2u9m"

# cloudinary media setups for images and videos
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'geetechlab-com',
#     'API_KEY': '622236724885358',
#     'API_SECRET': 'ZqOEAuVc4BLHp1bMkhxKJ51ye2s'
# }