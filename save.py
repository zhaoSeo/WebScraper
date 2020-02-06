# -*- coding: utf-8 -*- 

import csv

def save_to_file(jobs) :
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'])
    for job in jobs :
        print(list(job.values()))
        writer.writerow(list(job.values()))

    return