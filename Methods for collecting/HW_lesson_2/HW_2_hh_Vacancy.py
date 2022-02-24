import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
import json

vacancy = input(str("Какую вакансию ищем? >>> "))

main_site = "https://rostov.hh.ru/"

SEARCH_URL = f"{main_site}search/vacancy?clusters=true&area=76&ored_clusters=true&enable_snippets=true" \
             f"&salary=&text={vacancy}"

HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.82 Safari/537.36"
}

PARAMS = {"page": 0}


class HHScraper:
    def __init__(self, start_url, params, headers):
        self.headers = headers
        self.start_url = start_url
        self.start_params = params
        self.info_about_vacancy = []

    def run(self):
        self.get_vac_elements()
        for page_number in range(0, 3):
            params = self.start_params
            params["page"] = page_number
            self.get_vac_elements()

    @staticmethod
    def get_vacancy_list():
        try:
            r = requests.get(SEARCH_URL, params=PARAMS, headers=HEADERS)
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

        vac_list = self.get_vacancy_list()

        for vac in vac_list:
            vac_elements = {}
            vacancy_name = vac.find('span', {'class': 'g-user-content'})
            if vacancy_name is not None:
                try:
                    name = vac.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
                    show_name = name.getText()
                    link = vac.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
                    show_link = link['href']
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
                            min_salary = salaries[1]
                        elif "до" in salaries:
                            max_salary = salaries[1]

                        else:
                            min_salary = salaries[0]
                            max_salary = salaries[2]
                except AttributeError:
                    continue

                vac_elements['Vacancy'] = show_name
                vac_elements['Minimal salary'] = min_salary
                vac_elements['Maximum salary'] = max_salary
                vac_elements['link'] = show_link
                vac_elements['site'] = main_site

                self.info_about_vacancy.append(vac_elements)

            time.sleep(1)

        with open(file=f"{vacancy}_info", mode="w", encoding="utf-8") as file:
            json.dump(self.info_about_vacancy, file, ensure_ascii=False)
            pprint(self.info_about_vacancy)


if __name__ == "__main__":
    scraper = HHScraper(SEARCH_URL, PARAMS, HEADERS)
    scraper.run()
