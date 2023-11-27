from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

opts = Options()
opts.add_argument("--headless")

def scrape_single_page2list(url_page):
    driver = webdriver.Firefox(options=opts)
    driver.get(url_page)
    css_selector = f'li.modelLi:nth-child(1) > div:nth-child(1) > a:nth-child(2)'
    xpath_href = f'/html/body/div[5]/div[2]/div[6]/div[2]/ul/li[1]/div/div[2]'

    items = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_href)))
    # items = driver.find_elements(By.XPATH, xpath_href)
    for item in items:
        print(item.text)
    # print(items[0].get_attribute('href'))
    # for item in driver.find_elements(By.TAG_NAME, "a"):
    #     print(item)

    driver.quit()
    # return acronyms_dict

if __name__ == "__main__":
    url = "https://de.pornhub.com/pornstars/"
    driver = webdriver.Firefox(options=opts)
    scrape_single_page2list(url)

    # with open("/Users/antongigele/Desktop/python/spell_checker/csv_imports/porn_stars.csv", "w") as outfile: 
    #     wr = csv.writer(outfile,delimiter="\n")
    #     wr.writerow(pornstar_list)

    driver.quit()