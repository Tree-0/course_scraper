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
headers = [th.text.lower() for th in cs_course_rows[0].find_all('th')]

print(headers)

# course id : Course obj
courses = {}

# sort through the data and parse it into course objects
for row in cs_course_rows[1::]:

    # get data from every cell in the row
    course_data = list(row.find_all('td'))

    # assign course_id and name
    curr_course = course.Course(course_data[0].text, course_data[1].text)

    # add the current course to the dictionary
    courses[curr_course.course_id] = curr_course

    print(curr_course.course_id + " " + curr_course.title)

    # parse cells containing course times
    for i in range(2, len(course_data)):
        curr_course.parse(course_data[i], headers, i)
    

    print('\n')
