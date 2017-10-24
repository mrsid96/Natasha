def notify_self(request):
   token_app=facepy.utils.get_application_access_token('APP_ID','APP_SECRET_ID') 
   graph = GraphAPI(token_app)
   graph.post(
      path = 'me/notifications',
      template = '#Text of the notification',
      href = 'URL'
   ) 

   return HttpResponse('<script type=\'text/javascript\'>top.location.href = \'URL\'</script>')