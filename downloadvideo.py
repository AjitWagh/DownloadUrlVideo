import requests
from requests.auth import HTTPBasicAuth
import HTMLParser
#sudo apt-get install python-lxml
#pip install --upgrade lxml
from lxml import etree, html
parser = HTMLParser.HTMLParser()

SAVE_PATH = "/home/sagar/Ajit/Ajit_Sagar/DownloadUrlVideo"

#link of the video to be downloaded
links = open('links.txt','r')


def get_json_from_form(inp_str):
    form_dict = {}
    tree = html.fromstring(inp_str)
    action = tree.find(".//form").action
    form_dict['action'] = action
    inps= tree.findall(".//form//input[@type='hidden']")
    for inp in inps:
        form_dict[inp.name] = inp.value
        

    return form_dict
    
    

def download_file(url):
    local_filename = url.split('/')[-1]
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
    downl_url = session.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in downl_url.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


   

download_file("https://dcwater.ravnur.com/original/29346/4dbc004e-8341-4573-adc7-28a2097247e1.MPG")
