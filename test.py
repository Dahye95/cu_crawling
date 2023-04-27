from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

options = webdriver.ChromeOptions()

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'

options.add_argument('user_agent=' + user_agent)
# options.add_argument('headless')

url = 'https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


driver.get(url)

saleproduct = driver.find_elements_by_css_selector(
    '#contents > div.relCon > div > ul')

for i in saleproduct:
    list = i.text
    print(list)

time.sleep(10)

morebtn = driver.find_element_by_css_selector(
    '#contents > div.relCon > div > div > div.prodListBtn-w > a').click()

time.sleep(3)

saleproduct2 = driver.find_element_by_css_selector(
    '#contents > div.relCon > div > ul:nth-child(34)')

for i in saleproduct2:
    list2 = i.text
    print(list2)
