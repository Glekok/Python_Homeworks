from pprint import pprint
import requests
from lxml import html
from pymongo import MongoClient

M_HOST = "localhost"
M_PORT = 27017
M_DB = "News"
M_DB_COLLECTION = "Mail.ru_news"

HEADERS = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/98.0.4758.102 Safari/537.36"}

MAIN_NEWS_TITLE = '//td[contains(@class, "daynews__main")]//span/text()'
MAIN_NEWS_LINK = '//td[contains(@class, "daynews__main")]//a/@href'
MAIN_NEWS_2_TITLE = '//td[contains(@class, "daynews__items")]//span/text()'
MAIN_NEWS_2_LINK = '//td[contains(@class, "daynews__items")]//a/@href'
OTHER_NEWS_TITLE = "//a[contains(@class, 'list__text')]/text()"
OTHER_NEWS_LINK = "//a[contains(@class, 'list__text')]/@href"
DATETIME = '//span[contains(@class, "breadcrumbs__item")]//span/@datetime'
SOURCE = '//span[contains(@class, "note")]//span/text()'

news_list = []


def add_news_to_db(data):
    try:
        with MongoClient(M_HOST, M_PORT) as client:
            db = client[M_DB]
            collection = db[M_DB_COLLECTION]
            collection.insert_many(data)
            """При условии, что какие-то новости уже в базе
            for elements in data:
                new_link = str(elements["link"])
                for element in collection.find():
                    our_link = element["link"]
                    if our_link != new_link:
                        continue
                    else:
                        print("News already here!")
                        break
            collection.insert_one(elements)"""
            pprint(data)
    except TypeError as e:
        print(f"Что-то пошло не так >>> {e}")


def requests_to_mail_news(news, links, dates, sources):
    req_link = 'https://news.mail.ru/'
    r = requests.get(req_link, headers=HEADERS)
    root = html.fromstring(r.text)

    main_title = root.xpath(news)
    if main_title and len(main_title) > 0:
        link = root.xpath(links)
        for el in range(len(link)):
            r_link = requests.get(link[el], headers=HEADERS)
            root_2 = html.fromstring(r_link.text)
            source = root_2.xpath(sources)
            date = root_2.xpath(dates)
            news_dict = {'title': main_title[el].replace(u'\xa0', u' '), 'link': link[el],
                         'source': source[2], 'datetime': date[0]}
            news_list.append(news_dict)

    else:
        print('Странно, но похоже нет новостей!')

    # pprint(news_list)


if __name__ == "__main__":
    requests_to_mail_news(MAIN_NEWS_TITLE, MAIN_NEWS_LINK, DATETIME, SOURCE)
    requests_to_mail_news(MAIN_NEWS_2_TITLE, MAIN_NEWS_2_LINK, DATETIME, SOURCE)
    requests_to_mail_news(OTHER_NEWS_TITLE, OTHER_NEWS_LINK, DATETIME, SOURCE)
    add_news_to_db(news_list)
