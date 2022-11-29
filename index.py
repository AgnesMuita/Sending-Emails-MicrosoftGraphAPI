import os
import base64
import requests
from graph_api import generate_access_token


def draft_attachment(file_path):
  if not os.path.exists(file_path):
    print('file is not found')
    return 

  with open(file_path, 'rb') as upload:
    media_content=base64.b64encode(upload.read())

  data_body = {
    '@odata_type':'#microsoft.graph.fileAttachment',
    'contentBytes':media_content.decode('utf-8'),
    'name':os.path.basename(file_path)
  }
  return data_body

APP_ID='5a7a6b2d-77a0-4478-a4d2-cd2ccadf0463'
SCOPES=['Mail.Send', 'Mail.ReadWrite']

# for use with ConfidentialClientApplication
client_secret = "b9aadc3a-4734-4449-a65e-6ae9c968eb3a"
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'
endpoint = GRAPH_API_ENDPOINT+'/me'



access_token = generate_access_token(app_id=APP_ID, scopes=SCOPES)


headers={'Authorization':'Bearer' + access_token}

