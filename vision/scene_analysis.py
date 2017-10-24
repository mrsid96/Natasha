#Check the mood of the user.

import argparse
import base64
import simplejson as json

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
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        response = service_request.execute()

        x = "It might be "
        for i in range(0,len(response['responses'][0]['labelAnnotations'])):
            x += response['responses'][0]['labelAnnotations'][i]['description'] + ' or '

        x=x[:len(x)-4:]
        
        data = { 'data': x}
        fo = open("../main/pipe.ali","w")
        json.dump(data,fo)
        fo.close()
        print x

except:
    print 'Sorry couldnt connect to internet'