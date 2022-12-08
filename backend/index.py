import requests
from graph_api import generate_access_token
# from graph import generate_access_token
from attachments import requests_body

APP_ID='5a7a6b2d-77a0-4478-a4d2-cd2ccadf0463'
SCOPES=['Mail.Send', 'Mail.ReadWrite']
# for use with ConfidentialClientApplication
client_secret = "b9aadc3a-4734-4449-a65e-6ae9c968eb3a"
endpoint = 'https://graph.microsoft.com/v1.0/me/sendMail'



def send_email():
  access_token = generate_access_token(app_id=APP_ID, scopes=SCOPES)
  access_token_id=access_token['access_token']
  headers = {'Authorization': 'Bearer ' + access_token_id, 'Content_type':'application/json'}
  response=requests.post(endpoint, headers=headers, json=requests_body)
  print(response.json())

  if response.status_code==202:
    print('Email sent')
  else:
    print(response.reason)

send_email()