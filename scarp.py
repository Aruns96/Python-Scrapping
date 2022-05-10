import requests
from bs4 import BeautifulSoup

# importing beautiful Soup, which is used for scrapping the desired elements from the site.

print('Unknown Skills')
unknown=input(':')

# the site from which we are scrapping 

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text

# here lxml is the parser used 

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    skills = job.find('span', class_='srp-skills').text
    job_info = job.header.h2.a['href']
    if unknown not in skills:
        print(f'''
        Company Name : {company_name.strip()}
        Skills : {skills.strip()}
        Job Description : {job_info}
        ''')
        print('')