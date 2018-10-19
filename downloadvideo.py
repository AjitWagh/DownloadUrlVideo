import requests
from requests.auth import HTTPBasicAuth

def download_file(url):
    local_filename = url.split('/')[-1]
    session = requests.Session()
    
    payload = {'wa':'wsignin1.0',
               'wtrealm':'https://ravnurdcw.accesscontrol.windows.net/',
	       'wreply':'https://ravnurdcw.accesscontrol.windows.net/v2/wsfederation',
	       'wctx':'cHI9d3NmZWRlcmF0aW9uJnJtPWh0dHBzJTNhJTJmJTJmZGN3YXRlci5yYXZudXIuY29tJTJmJmN4PSUyZkRlZmF1bHQuYXNweA2'
	      }

    headers = {'Content-Type':'application/x-www-form-urlencoded',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,  
	   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
	      }
    data = {'UserName':'testlead@dcwater.com',
	    'Password':'Wipro123$',
	    'AuthMethod':'FormsAuthentication'}
    resp = session.post("https://sts.dcwater.com/adfs/ls/",params=payload,headers=headers,data = data)
    headers.pop("Content-Type", "")
    resp1 = session.get(url, stream=True, headers = headers)
    import pdb; pdb.set_trace()	

    # NOTE the stream=True parameter
    # requests.get(url, auth=HTTPBasicAuth('testlead', 'Wipro123$'), stream=True)
    #r = requests.get(url, stream=True)
    
    with open(local_filename, 'wb') as f:
        for chunk in resp1.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

download_file("https://dcwater.ravnur.com/original/29346/4dbc004e-8341-4573-adc7-28a2097247e1.MPG")
