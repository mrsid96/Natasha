
import facebook
import requests

token = 'MY_TOKEN'

graph = facebook.GraphAPI(token)
group = graph.get_object('GROUP_ID')

posts = graph.get_connections(id='GROUP_ID', connection_name='feed')
all_posts = []
while(True):
    try:
        for post in posts['data']:
            all_posts.append(post['message'].encode('utf-8'))
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break
print len(all_posts) # always 10