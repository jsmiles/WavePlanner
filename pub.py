import requests
from bs4 import BeautifulSoup

def pub_parser(city):
    response = requests.get(f'https://whatpub.com/search?q={ city }&t=ft&p=1')
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.select('.pub_details')[0].find('a').get_text()
    return res
