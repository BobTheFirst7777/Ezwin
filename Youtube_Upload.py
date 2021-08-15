import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret_833755492025-mnjbmn7je0s2grls9gtpqq8hkfado60k.apps.googleusercontent.com.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

upload_date_time = datetime.datetime(2021, 8, 15, 14, 00, 0).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryI': 20,
        'title': 'Test Upload',
        'description': 'Please work god please',
        'tags': ['Creeper', 'Video Game']
    },
    'status': {
        'privacyStatus': 'public',
        #'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('Vsauce.MP4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()


service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('ThumbnailSample.png')
).execute()
