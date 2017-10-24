#Check the mood of the user.

import argparse
import base64
import simplejson as json
import os

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
                    'type': 'TEXT_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        response = service_request.execute()
        x = response['responses'][0]['fullTextAnnotation']['text']
        x = str(x).replace('\n','. ').lower()
        data = { 'data': x}
        fo = open("../main/pipe.ali","w")
        json.dump(data,fo)
        fo.close()
except:
    print 'Sorry couldnt connect to internet'
