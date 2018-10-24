import requests
from requests.auth import HTTPBasicAuth
import HTMLParser
#pip install --upgrade lxml
from lxml import etree, html
from bs4 import BeautifulSoup
import uuid
parser = HTMLParser.HTMLParser()
#sudo apt-get install python-lxml

#SAVE_PATH = "/home/sagar/Ajit/Ajit_Sagar/DownloadUrlVideo"

#link of the video to be downloaded
#links = open('links.txt','r')


def get_json_from_form(inp_str):
    form_dict = {}
    tree = html.fromstring(inp_str)
    action = tree.find(".//form").action
    form_dict['action'] = action
    inps= tree.findall(".//form//input[@type='hidden']")
    for inp in inps:
        form_dict[inp.name] = inp.value
        

    return form_dict
    
    

def download_file(video_link):
    
    session = requests.Session()
    
    params = {'wa':'wsignin1.0',
               'wtrealm':'https://ravnurdcw.accesscontrol.windows.net/',
	       'wreply':'https://ravnurdcw.accesscontrol.windows.net/v2/wsfederation',
	       'wctx':'cHI9d3NmZWRlcmF0aW9uJnJtPWh0dHBzJTNhJTJmJTJmZGN3YXRlci5yYXZudXIuY29tJTJmJmN4PSUyZkRlZmF1bHQuYXNweA2'
	      }
  
    headers = {'Content-Type':'application/x-www-form-urlencoded'
	      }
    payload = {'UserName':'testlead@dcwater.com',
	    'Password':'Wipro123$',
	    'AuthMethod':'FormsAuthentication'}
    resp = session.post("https://sts.dcwater.com/adfs/ls",params=params,headers=headers,data = payload, verify=False)
    #rep_cont = parser.unescape(resp.text)
    #import pdb; pdb.set_trace()
    form_data = get_json_from_form(resp.content)
    action = form_data.pop('action')
    resp1 = session.post(action,headers=headers,data=form_data, verify=False)
    form_data = get_json_from_form(resp1.content)
    action = form_data.pop('action')
    resp2 = session.post(action,headers=headers,data=form_data, verify=False)

    video = open('/home/sagar/AJ/links.txt','r')
    
    for link in video:
    	link = link.strip("\n").strip('\r')
    	file_name = link.split('/')[-1]
    	ext = file_name.split('.')[-1]	
    	local_filename =  file_name + "_" + str(uuid.uuid4()) + '.' + ext
    	print "Downloading file:%s"%local_filename
    	r = session.get(link, stream=True)
        
        #print(link[-1])

    	with open(local_filename, 'wb') as f:
        	for chunk in r.iter_content(chunk_size=1024):
        		if chunk:  # filter ou
        		    f.write(chunk) #f.flush() commented by recommendation from J.F.Sebastian
    #print "%s downloaded!\n"%local_filename

    #print "All videos downloaded!"

    return local_filename


download_file('link')
