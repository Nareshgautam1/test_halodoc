import requests


url = "https://api.restful-api.dev/objects/ff80818192925da70192999369861369"
file = open("../data/update_obj.json", 'r')
header = {'accept': 'application/json',
              'Content-Type': 'application/json'}
request_body = file.read()
response = requests.put(url=url,headers=header, data=request_body)
data = response.json()
print(data["data"]['Hard disk size'])