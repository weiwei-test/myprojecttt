import requests

url = 'http://localhost:9528/size/list'
params = {"skc":"1111"}
res = requests.get(url,params=params)
print(res.text)