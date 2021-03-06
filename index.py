from direct_cloud_box.api import directCloudBox
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER_SERVICE = os.environ.get("SERVICE")
USER_SERVICE_KEY = os.environ.get("SERVICE_KEY")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
USER_ID = os.environ.get("USER_ID")
PASSWORD = os.environ.get("PASSWORD")

user_api = directCloudBox(
    USER_SERVICE,
    USER_SERVICE_KEY,
    COMPANY_CODE,
    USER_ID,
    PASSWORD
    )
try:
    # print(user_api.folderCreate("test", "1"))
    # print(user_api.folderGet(""))
    print(user_api.folderGet("1"))
    # print(user_api.folderGet("SharedBOX"))
    # print(user_api.fileUpload("./sample_file/sample_movie.mp4", "1"))
    print(user_api.fileGet("1"))
    
    print(user_api.fileDownloadUrl("1", "285389469"))
    print(user_api.fileViewer("285389469"))


    
    
finally:
    user_api.tokenExpire()