# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/취업?q=web&l=부산&limit=10")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all("a")

pages = []

for link in links[:-1]:
    pages.append(int(link.find("span").string))
max_page = pages[-1]