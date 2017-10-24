import feedparser, time, sys, os
 
#these are the RSS URLs to parse
fbURL = "http://www.facebook.com/feeds/notifications.php?id=1643658315938139"
#replace the above FB link with your personal FB RSS feed URL which you will find here:
#https://www.facebook.com/notifications
 
fbFeed = feedparser.parse(fbURL)["channel"] #parse the fb feed
fbUpdated = fbFeed.updated # extract the date/time of the last update
 
#start a loop
while True:
     
####### FACEBOOK #########
    fbFeed_new = feedparser.parse(fbURL)["channel"]
    if fbFeed_new.updated > fbUpdated: #checks if RSS feed has been updated
        print("New feed in facebook")
        #end for
        fbUpdated = fbFeed_new.updated
    #end if
