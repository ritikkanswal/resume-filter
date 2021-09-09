import requests

url ='http://127.0.0.1:8000/studentapi/'
path='r.pdf'
data={'name':"Riitik"}
files = {'file': open(path, 'rb')}
r = requests.post(url,data=data,files=files)
print(r.json())