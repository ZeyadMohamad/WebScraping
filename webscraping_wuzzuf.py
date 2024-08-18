import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

title = []
company = []
location = []
skill = []
link = []
salary = []
responsibilities = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=Data%20Scientist&a=hpb")

src = result.content

#scraping data from main page
soup = BeautifulSoup(src, "html.parser")

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
print(job_titles)

company_names = soup.find_all("a", {"class" : "css-17s97q8"})
print(company_names)

location_names = soup.find_all("span", {"class" : "css-5wys0k"})
print(location_names)

job_skills = soup.find_all("div", {"class" : "css-y4udm8"})
print(job_skills)

for i in range(len(job_titles)):
    title.append(job_titles[i].text)
    company.append(company_names[i].text)
    location.append(location_names[i].text)
    skill.append(job_skills[i].text)
    link.append(job_titles[i].find("a").attrs['href'])

for i in link:
    res = requests.get(i)
    src = res.content
    soup = BeautifulSoup(src, "html.parser")
    salaries = soup.find_all("div", {"class" : "css-4xky9y"})
    

salary = ["confidential"] * len(title)

#saving scraped data to csv file
file_list = [title, company, location, skill, link, salary]
export = zip_longest(*file_list)
with open("D:/webscraping.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title", "company name", "location", "skills", "links", "salary"])
    wr.writerows(export)
