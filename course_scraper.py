'''
course_scraper.py
Scrape the data of NU course catalog information and use it to plan future class schedules. 
'''

import requests
from bs4 import BeautifulSoup
import course

CS_URL = 'https://www.mccormick.northwestern.edu/computer-science/academics/courses/'
#IEMS_URL = 'https://www.mccormick.northwestern.edu/industrial/academics/courses/'

# get data from cs and iems websites
cs_response = requests.get(CS_URL)
#iems_response = requests.get(IEMS_URL)

cs_html = cs_response.text
#iems_html = iems_response.text

# parse content
cs_soup = BeautifulSoup(cs_html, 'html.parser')
#iems_soup = BeautifulSoup(iems_html, 'html.parser')

cs_course_table = cs_soup.find(id='course_list')
cs_course_rows = cs_course_table.find_all('tr')

# get labels from table
headers = [th.text for th in cs_course_rows[0].find_all('th')]

print(headers)

# course id : Course obj
courses = {}

# sort through the data and parse it into course objects
for i,row in enumerate(cs_course_rows[1::]):
    course_data = [td.text for td in row.find_all('td')]
    print(course_data)

    curr_course = course.Course(course_data[0], course_data[1])
    break


