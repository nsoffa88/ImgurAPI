#basic networking imports
from pprint import pprint
import requests
import json
 
#image handling imports
import base64
 
#your api key will go here, as a string
api_key = '60a9f235e6726aa'
 
#here's the API url that you'll need to POST to
url = r'http://api.imgur.com/2/upload.json'
 
#full image path
image_path = 'venom.jpg'
 
#open binary data, instead of regular read
f = open(image_path, 'rb')
 
#encode image file for transfer
binary_data = f.read()  #again, not string data, but binary data
b64image = base64.b64encode(binary_data)
 
#data to send with the POST request
payload = {'key' : api_key,
           'image': b64image,
           'title': 'apitest',}  #title of image as seen on imgur.com
 
#make the POST request, with the attached data of payload
r = requests.post(url, data=payload)
 
#turn the returned json into a python dict
j = json.loads(r.text)
 
#print it out cleanly
pprint(j)