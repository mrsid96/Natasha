graph = facebook.GraphAPI(token.token)
connection_type = 'feed'
total_posts = 0
try:
    feed = graph.get_connections('me', connection_type, limit=1000)
    while 'paging' in feed and 'next' in feed['paging'] and feed['paging']['next']:
        total_posts += len(feed['data'])
        print 'celery_count_facebook_posts @ %s total_posts' % (total_posts,)
        nextUrl = feed['paging']['next']
        parsed = urlparse.urlparse(nextUrl)
        until = int(urlparse.parse_qs(parsed.query)['until'][0])
        feed = graph.get_connections('me', connection_type, limit=1000, until=until)
    total_posts += len(feed['data'])
    print 'celery_count_facebook_posts FINISHED @ %s total_posts' % (total_posts,)