import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
from pymongo import MongoClient

vacancy = input(str("Какую вакансию ищем? >>> "))

main_site = "https://rostov.hh.ru/"

SEARCH_URL = f"{main_site}search/vacancy?clusters=true&area=76&ored_clusters=true&enable_snippets=true" \
             f"&salary=&text={vacancy}"

HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36"
}

PARAMS = {"page": 0}

M_HOST = "localhost"
M_PORT = 27017
M_DB = "Vacancies"
M_DB_COLLECTION = "vacancies_from_hh"


def show_need_salary():
    salary_needed = int(input("Свыше какой суммы ищем вакансии? >>> "))
    with MongoClient(M_HOST, M_PORT) as client:
        db = client[M_DB]
        collection = db[M_DB_COLLECTION]
        for el in collection.find({"Minimal_salary": {"$gt": salary_needed}}).sort("Vacancy"):
            pprint(el)


class HHScraper:
    def __init__(self, start_url, params, headers):
        self.headers = headers
        self.start_url = start_url
        self.start_params = params

    def run(self):
        how_much_pages = int(input("Сколько страниц будем исследовать? >>> "))
        for page_number in range(0, how_much_pages):
            params = self.start_params
            params["page"] = page_number
            self.get_vac_elements()

    def get_vacancy_list(self, url, params):
        try:
            r = requests.get(url, params, headers=self.headers)
            r.raise_for_status()
            parse_r = BeautifulSoup(r.text, "html.parser")
            vac_block = parse_r.find('div', {'class': 'vacancy-serp'})
            vac_list = vac_block.findChildren(recursive=False)
        except Exception as e:
            time.sleep(1)
            print(e)
            return None
        return vac_list

    def get_vac_elements(self):

        vac_list = self.get_vacancy_list(self.start_url, self.start_params)
        vacancies = []
        for vac in vac_list:
            vac_elements = {}
            vacancy_name = vac.find('span', {'class': 'g-user-content'})
            if vacancy_name is not None:
                try:
                    name = vac.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
                    show_name = name.getText()
                    link = vac.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
                    show_link = link['href']
                    vac_id = show_link.rstrip('/').split('/')[-1].split("?")[0]
                    salary = vac.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
                    if not salary:
                        min_salary = "salary not specified"
                        max_salary = "salary not specified"
                    else:
                        show_salary = salary.getText().replace('\u202f', '')

                        min_salary = None
                        max_salary = None
                        salaries = show_salary.split(' ')
                        if 'от' in salaries:
                            min_salary = int(salaries[1])
                        elif "до" in salaries:
                            max_salary = int(salaries[1])

                        else:
                            min_salary = int(salaries[0])
                            max_salary = int(salaries[2])
                except AttributeError:
                    continue

                vac_elements['Vacancy'] = show_name
                vac_elements['vac_id'] = vac_id
                vac_elements['Minimal_salary'] = min_salary
                vac_elements['Maximum_salary'] = max_salary
                vac_elements['link'] = show_link
                vac_elements['site'] = main_site

                vacancies.append(vac_elements)

            time.sleep(1)

        self.vacancies_adding(vacancies)

    @staticmethod
    def vacancies_adding(data):
        try:
            with MongoClient(M_HOST, M_PORT) as client:
                db = client[M_DB]
                collection = db[M_DB_COLLECTION]
                collection.insert_many(data)
        except TypeError as e:
            print(e)
            return None


if __name__ == "__main__":
    scraper = HHScraper(SEARCH_URL, PARAMS, HEADERS)
    scraper.run()
    show_need_salary()
