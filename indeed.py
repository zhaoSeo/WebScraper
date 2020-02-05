# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/취업?q=web&l=부산&limit={LIMIT}"

def extract_pages() :
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))

    max_page = pages[-1]

    return max_page

def extract_job(html) :
    title = html.find("div", {"class" : "title"}).find("a")["title"]
    company = html.find("span", {"class" : "company"}).string.strip()
    
    # company_anchor = company.find("a")
    # if company_anchor is not None :
    #     print(company_anchor.string)
    # else :
    #     print(company.string)

    location = html.find("div", {"class" : "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://kr.indeed.com/채용보기?jk={job_id}"}
    

def extract_jobs(last_page) :
    jobs = []
    for page in range(last_page) :
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        for result in results :
            job = extract_job(result)
            print(job)
            jobs.append(job)
    return jobs

def get_jobs() : 
    last_page = extract_pages()
    jobs = extract_jobs(last_page)
    return jobs
