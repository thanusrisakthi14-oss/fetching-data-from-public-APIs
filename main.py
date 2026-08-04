import requests
url="https://v2.jokeapi.dev/joke/Any?format=json"
response=requests.get(url)
data=response.json()
if 'setup' in data:
    print(data['setup'])
if 'delivery' in data:
    print (data['delivery'])