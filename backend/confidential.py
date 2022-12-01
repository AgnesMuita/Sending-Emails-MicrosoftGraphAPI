import webbrowser
from datetime import datetime
import json
import os
import msal
import requests

client_secret = "noX8Q~-fZq_RHI9n..EhrP11EH8pZNSBb6K6AcEA"
authority_url = "https://login.microsoftonline.com/consumers/"
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'
endpoint = GRAPH_API_ENDPOINT+'/me'

APP_ID='5a7a6b2d-77a0-4478-a4d2-cd2ccadf0463'
SCOPES=['Mail.Send', 'Mail.ReadWrite']

def generate_access_token(app_id,scopes):
  client_instance = msal.ConfidentialClientApplication(client_id=app_id, client_credential=client_secret)
  authorization_url=client_instance.get_authorization_request_url(scopes)
  webbrowser.open(authorization_url, new=True)
  authorization_code = "0.AQkAhaJScwsKk0OfyGTwFJz-_C1relqgd3hEpNLNLMrfBGMJAPs.AgABAAIAAAD--DLA3VO7QrddgJg7WevrAgDs_wQA9P8jx63MNLMy7351FFtfGuHYi1SkB2r02BZ_1IF9Z1oVWOPlPtmzbjDsUEzAzUmSC_lC8AaT78p9nRBOQV_nZwUridMwwb0zeccWdGaLknSkt7e0qZR0_vgK6DfhGfBG96ptMfiZ0ibEr8i98TfJ7UeCME2oMWI_PURg45ETX4EnFnHLug9qLuEBe7xPIl9b4D2x2soJ0VcoYeB6IJqz4sdnroa__JiCuQgH7xACMdRj79S6LLW26zoiWQlJXaCw3h6nfDSQlp1rSr4oFWSv6b5TwTyIJNVXQGcxmR--jZ-IrpdzLiZpmH72PtXz-gHmS4vKnDX6WyPqnHydykVUhGe-9K6YN3Nqy_NgjKEBS2zgT893NWiQrFL6uSiN9BdpNiNlVzME6W5xrx75OrYJbqvwp05K2SWQjvOr6Zkw-nJ3M1yUWPH1_hNow2lb1YRvXYjCDZmKSuJPNUpvy6V1cNcwH1TL8r2sykbwWOGKQ3vjmg_34gG4DASa3dWWBwQ74VyFXmXpw4fSqdVOdrJjEhVow_aEAHEmRyo-wwfCW4NAr2z3dxlNqThvGu5R-FJkQ6uKtfhwUx93wU8PHkQCZ1tdLTlpYoVPv-aR4s_iHxRpdRUM1QccY4PPHPji3BcLe3xeXduINabiop3bEgCDa6yiJiCouSychnZSrbm8rYZwg3G-mpKbOPNNBy6LLXAgR730peuECMZ6YGTKXp5QyzaT6fDSVvRCvQ8Z_uFMGELTURqumHWU2BWJkLs-JnNpSFml"
  access_token = client_instance.acquire_token_by_authorization_code(code=authorization_code, scopes= scopes)
  print(access_token)
  access_token_id=access_token['access_token']
  headers={'Authorization':'Bearer' + access_token_id}
  response=requests.get(endpoint, headers=headers)
  return response

  # with open('ms_graph_api_token.json', 'w') as _f:
  #   _f.write(access_token_cache.serialize())

access_token = generate_access_token(app_id=APP_ID, scopes=SCOPES)
if __name__ == '__main__':
    ...



