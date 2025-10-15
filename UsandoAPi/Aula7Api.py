import json 
import requests



username="YanGabrielton"
url=f"https://api.github.com/users/{username}"

response=requests.get(url)
print(f'mostrando Resultado da busca{response.status_code}')

if response.status_code == 200:
    data=   response.json()
    print(json.dumps(data,indent=2))
    
    
if response.status_code == 200:
    print(f"mostrando o site admin : {data.get('site_admin')}")