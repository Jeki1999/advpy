from bs4 import BeautifulSoup
from fake_headers import Headers
import requests 


def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()


response = requests.get('https://habr.com/ru/all/', headers=get_headers())

habr_main = response.text

soup = BeautifulSoup(habr_main, features='lxml')

article_list = soup.find('div', class_='tm-articles-list')
articles = article_list.find_all('article')

parsed = []

for article in articles:
    time_tag = article.find('time')
    header = article.find('h2')
    time_parsed = time_tag['datetime']
    header_parsed = header.text

    a_tag = header.find('a')
    link_related = a_tag['href']
    link_absolute = f'https://habr.com{link_related}'

    
    
