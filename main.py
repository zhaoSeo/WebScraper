# -*- coding: utf-8 -*- 

import requests

indeed_result = requests.get("https://kr.indeed.com/취업?q=web&l=부산&limit=50")

print(indeed_result.text)