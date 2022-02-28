from pprint import pprint
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import trange
from selenium.webdriver.support.ui import Select
from urllib.parse import urljoin

SEARCH_WINDOW_XPATH = "//li[contains(@class, '_wall_tab_own')]//a"
SEARCH_FIELD_XPATH = "//input[contains(@class, 'ui_search_field')]"
POST_LINK_XPATH = "//a[contains(@class, 'post_link')]"
POST_DATE_XPATH = "//span[contains(@class, 'rel_date')]"
POST_TEXT_XPATH = "//div[contains(@class, 'wall_post_text')]"
LIKES_COUNT_XPATH = "//div[contains(@class, 'PostButtonReactions__title')]"
SHARE_COUNT_XPATH = "//span[contains(@class, 'blind_label')]"
VIEW_COUNT_XPATH = "//div[contains(@class, 'like_views')]"  # //@title"

URL = "https://vk.com/tokyofashion"
DRIVER_PATH = "./chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get(URL)

# to_find = input("Что будем искать? >>> ")


search_window = driver.find_element_by_xpath(SEARCH_WINDOW_XPATH).get_attribute("href")

driver.get(search_window)

search_field = driver.find_element_by_xpath(SEARCH_FIELD_XPATH)
search_field.send_keys(f"кеды" + '\n')
# driver.implicitly_wait(2)

post_text = driver.find_element_by_xpath(POST_TEXT_XPATH).text
print(post_text)

likes_count = driver.find_element_by_xpath(LIKES_COUNT_XPATH).text
print(likes_count)
