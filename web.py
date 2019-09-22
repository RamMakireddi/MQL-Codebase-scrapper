from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import Request, urlopen
from selenium import webdriver
import re

browser = webdriver.Chrome()

 
site = "https://www.mql5.com/en/code/mt4/indicators/page36"
hdr = {'User-Agent': 'Chrome/7.6'}
req = Request(site,headers=hdr)
page = urlopen(req)
page_soup = soup(page, "html.parser")

browser.get(site)

list_of_hrefs = []

content_blocks = browser.find_elements_by_class_name("title")

for block in content_blocks:
    elements = block.find_elements_by_tag_name("a")
    for el in elements:
        list_of_hrefs.append(el.get_attribute("href"))
for href in list_of_hrefs:
	browser.get(href)
	try:
		names = browser.find_elements_by_partial_link_text(".mq4")
		for name in names:
			name.click()
	except:
		pass

