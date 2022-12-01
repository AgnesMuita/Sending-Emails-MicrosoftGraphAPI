import os
import base64

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


requests_body = { 
  'message':{
    'toRecipients':[
      {
        'emailAddress':{
          'address':'wamwithamuita1996@outlook.com'
        }
      }
    ],
    'subject':'Greetings! Howdy! ',
    'importance':'normal',
    'body':{
      'contentType':'HTML',
      'content':'<b>Be Awesome. Regards, Aggie</b>'
    },
    'attachments':[
      draft_attachment('Document 1-converteds.pdf')
    ]
  }
} 