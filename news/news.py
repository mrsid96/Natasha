from lxml import html
import requests
import simplejson as json

try:
	# Send request to get the web page
	response = requests.get('http://news.google.co.in')

	# Check if the request succeeded (response code 200)
	if (response.status_code == 200):

	    # Parse the html from the webpage
	    pagehtml = html.fromstring(response.text)

	    # search for news headlines
	    news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
	                          /a/span[@class="titletext"]/text()')
	    
	# Print each news item in a new line
	print '\n'.join(news[0:5:])
	new = {
			'data':'. '.join(news[0:5:])
			}
	fo = open("../main/pipe.ali","w")
	json.dump(new,fo)
	fo.close()
except:
	print 'Sorry Sir, Couldnt fetch news, right now'