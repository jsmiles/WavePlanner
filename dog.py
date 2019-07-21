import requests

def doggo():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return data['message']
