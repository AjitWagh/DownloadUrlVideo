#importing the module
import urllib2
import requests
from requests.auth import HTTPBasicAuth

#define the url
url = 'https://dcwater.ravnur.com/video/29379/MobileM.mp4'

#Add your headers

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}

# Create the Request. 
request = urllib2.Request(url, None, headers)

# Getting the response
response = urllib2.urlopen(request)
 
print response.headers