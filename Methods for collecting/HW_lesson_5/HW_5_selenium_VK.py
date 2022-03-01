from pprint import pprint
from random import randint

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import trange
from selenium.webdriver.support.ui import Select
from urllib.parse import urljoin
import time

SEARCH_WINDOW_XPATH = "//li[contains(@class, '_wall_tab_own')]//a"
SEARCH_FIELD_XPATH = "//input[contains(@class, 'ui_search_field')]"
POST_DATE_XPATH = "//span[contains(@class, 'rel_date')]"
POST_TEXT_XPATH = "//div[contains(@class, 'wall_post_text')]"
POST_LINK_XPATH = "//a[contains(@class, 'post_link')]"
LIKES_COUNT_XPATH = "//div[contains(@class, 'PostButtonReactions__title')]"
SHARE_COUNT_XPATH = "//div[contains(@class, 'PostBottomAction PostBottomAction--withBg share _share')]"
VIEW_COUNT_XPATH = "//div[contains(@class, 'like_views')]"
# BAD_WINDOW_XPATH = "//a[contains(@class, 'JoinForm__notNowLink')]"


URL = "https://vk.com/tokyofashion"
DRIVER_PATH = "./chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get(URL)

# to_find = input("Что будем искать? >>> ")
time.sleep(2)

search_window = driver.find_element_by_xpath(SEARCH_WINDOW_XPATH).get_attribute("href")

driver.get(search_window)
time.sleep(2)
search_field = driver.find_element_by_xpath(SEARCH_FIELD_XPATH)
search_field.send_keys(f"nike" + '\n')
time.sleep(3)


def get_posts_info():
    try:
        posts_dict = {}

        post_date = driver.find_element_by_xpath(POST_DATE_XPATH).text
        posts_dict['date'] = post_date.replace("&nbsp;", ' ') if post_date else None

        post_text = driver.find_element_by_xpath(POST_TEXT_XPATH).text
        posts_dict['text'] = post_text.replace("\n", " ") if post_text else None

        post_link = driver.find_element_by_xpath(POST_LINK_XPATH).get_attribute("href")
        posts_dict['link'] = post_link if post_link else None

        post_likes = driver.find_element_by_xpath(LIKES_COUNT_XPATH).text
        posts_dict['likes'] = post_likes if post_likes else None

        post_shares = driver.find_element_by_xpath(SHARE_COUNT_XPATH).get_attribute("aria-label")
        posts_dict['reposts'] = post_shares if post_shares else None

        post_views = driver.find_element_by_xpath(VIEW_COUNT_XPATH).get_attribute("title")
        posts_dict['views'] = post_views if post_views else None
        pprint(posts_dict)

    except Exception as e:
        print(e)


get_posts_info()
