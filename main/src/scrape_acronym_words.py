import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json

opts = Options()
opts.add_argument("--headless")

def scrape_all_pages(url):
    complete_acronym_dict = {}
    for j in range(1, 10+1):
        url_with_subpage = url+str(j)
        complete_acronym_dict.update(scrape_single_page2dict(url_with_subpage))

    return complete_acronym_dict

def scrape_single_page2dict(url_page):
    driver = webdriver.Firefox(options=opts)
    driver.get(url_page)
    xpath_single_entry = f'//*[@id="common-terms"]/table/tbody/tr[{1}]/td[{3}]'
    xpath_tbody = f'//*[@id="common-terms"]/table/tbody'
    acronyms_dict = {}
    for i in range(1, 20+1):
        xpath_href = f'//*[@id="common-terms"]/table/tbody/tr[{i}]/td[2]/div/a'

        items = driver.find_elements(By.XPATH, xpath_href)
        acronyms_dict[items[0].get_attribute('href').split("/")[-2]] = items[0].get_attribute('href').split("/")[-1]
        print(items[0].get_attribute('href').split("/")[-2])
        print(items[0].get_attribute('href').split("/")[-1])

    driver.quit()
    return acronyms_dict

if __name__ == "__main__":
    url = "https://www.allacronyms.com/porn/abbreviations/"
    driver = webdriver.Firefox(options=opts)

    with open("/Users/antongigele/Desktop/python/spell_checker/csv_imports/porn_acronyms.json", "w") as outfile: 
        json.dump(scrape_all_pages(url), outfile)

    driver.quit()
