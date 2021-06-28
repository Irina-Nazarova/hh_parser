import requests
from bs4 import BeautifulSoup
import csv

HOST = "https://chusovoi.hh.ru"
URL = "https://chusovoi.hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=Python+Backend+Developer"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "accept": "*/*",
}
FILE = "hh.csv"


def get_html(url, params=None):
    """Функция для получения контента с указанного url."""
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='vacancy-serp-item vacancy-serp-item_premium')
    vacancies =[]

    for item in items:
        vacancies.append(
            {
                "title": item.find("div", class_="vacancy-serp-item__info",).get_text(strip=True),
                "company": item.find("div", class_="vacancy-serp-item__meta-info-company",).get_text().replace("\xa0", " "),
                "city": item.find("span", class_="vacancy-serp-item__meta-info",).get_text(strip=True),
                "link": item.find("a", class_="bloko-link",).get('href'),
             }
        )
    return vacancies


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print('Error')

parser()




# html = get_html(URL)
# print(get_content(html.text))