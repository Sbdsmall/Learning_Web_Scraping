import requests
response = requests.get('https://developer.riotgames.com')
print(response.text)