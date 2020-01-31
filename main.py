# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/취업?q=web&l=부산&limit=10")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all("a")

spans = []

for page in pages:
    spans.append(page.find("span"))
spans = spans[:-1]