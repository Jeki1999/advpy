from bs4 import BeautifulSoup
from fake_headers import Headers
import requests 
import json

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()


response = requests.get('https://spb.hh.ru/search/vacancy?text=python+flask+djiango&salary=&area=1&area=2&ored_clusters=true', headers=get_headers())
hh_main = response.text
soup = BeautifulSoup(hh_main, features='lxml')

vacancies = soup.find_all('div', class_="vacancy-serp-item-body__main-info")

parsed = []

for vacancion in vacancies:
    link = vacancion.find(class_="serp-item__title")['href']
    try:
        salary = vacancion.find('span', class_="bloko-header-section-3").text
    except:
        salary = 'Не указано'
    company = vacancion.find(class_="bloko-link bloko-link_kind-tertiary").text
    city = soup.find('div', class_="vacancy-serp-item__info").find(attrs= {"data-qa": "vacancy-serp__vacancy-address"}, class_="bloko-text").text


    item = {
        'link' : link,
        'salary' : salary,
        'company' : company,
        'city' : city
    }
    parsed.append(item)



with open ('hh.json', 'w') as file:
    json.dump(parsed, file, indent=5)

