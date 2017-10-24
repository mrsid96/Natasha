#Check the mood of the user.

import argparse
import base64
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('vision', 'v1', credentials=credentials)

try:
    with open('../main/image.jpg', 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LANDMARK_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        response = service_request.execute()

        response = response['responses'][0]['landmarkAnnotations'][0]['description']

        data = { 'data': 'It is '+response}
        fo = open("../main/pipe.ali","w")
        json.dump(data,fo)
        fo.close()
        
except:
    print 'Sorry Couldnt connect to internet'
