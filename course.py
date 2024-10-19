'''
Module providing an object to represent university classes, and methods to add, edit, 
and remove information about those classes
'''

import re
import time_span

class Course:
    '''
    Represents one university course, containing information about the name and id of the course,
    as well as what quarters, days, and times the course is offered. 
    '''
    def __init__(self, course_id: str, title: str):
        self.course_id = course_id  # e.g. COMP_SCI 150
        self.title = title  # e.g. Intro to Computer Science
        self.year = -1 # course year

        # Classes are offered in specific quarters with days and times
        # Default: no classes scheduled for any quarter
        self.quarter_to_days = {'fall': None, 'winter': None, 'spring': None, 'summer': None}

        # Example structure for each quarter:
        # {'M': None, 'Tu': None, 'W': None, 'Th': None, 'F': None}

        # Each day's schedule will contain a TimeSpan (start_hr, start_mnt, end_hr, end_mnt)


    def add_days_to_quarter(self, quarter, days):
        '''
        given a quarter (str) and list of days (strs), add these days to the list of 
        offered days in the quarter
        '''

        # if no days have been added to quarter, create empty dict
        if self.quarter_to_days[quarter] is None:
            self.quarter_to_days[quarter] = {}

        # create an empty dict for every day in the quarter.
        # Times will be added to these dictionaries.
        for day in days:
            self.quarter_to_days[quarter].append({day:None})


    def add_time_to_day(self, quarter, day, time):
        '''
        Given a quarter (str), a day (str), and a time (TimeSpan), 
        add the offered time to the course object.
        '''
        # If no days have been added to the quarter, create an empty dictionary for the quarter
        if self.quarter_to_days[quarter] is None:
            self.quarter_to_days[quarter] = {}

        # If the day does not exist in the quarter's dictionary, initialize it as an empty list
        if day not in self.quarter_to_days[quarter]:
            self.quarter_to_days[quarter][day] = []

        # Add the time to the list of times for that day
        self.quarter_to_days[quarter][day].append(time)


    
    def parse_row(self):
        pass


    def parse_cell(self, html, column_headers, index):
        '''
        Given the scraped html data for a cell, parse it into quarters, days, and times...
        '''
        html_stripped = html.stripped_strings
        text_parts = list(html_stripped)
        # print(text_parts)

        if not text_parts:
            return
            #print(f'{column_headers[index]}: class not offered')
        else:
            # regex to find the times the course is offered
            time_pattern = r'\b\d{1,2}(?::\d{2})?-\d{1,2}(?::\d{2})?\b'
            times = re.findall(time_pattern, text_parts[0])

            # regex to find the days the course is offered
            days = None
            if (text_parts[0] != 'TBD'):
                day_pattern = r'(Th|Tu|T|M|W|F)'
                days = re.findall(day_pattern, text_parts[0])
            
            # if class has a lab section, the html will have a third text part
            # lab_times = None
            # lab_day = None
            # if len(text_parts) == 3:
            #     lab_times = re.findall(time_pattern, text_parts[2])
            #     lab_day = re.findall(day_pattern, text_parts[2])

            # print
            # print(column_headers[index] +": ", end='')
            
            # if not times:
                # print('No times specified. ', end='')
            # else:
                # print(times, end='')
            # if lab_times:
            #     print(lab_times, end='')
            
            # if not days:
                # print('No days specified. ', end='')
            # else:
                # print(days, end='')
            # if lab_day:
            #     print(lab_day, end='')

            # print()

            # find the corresponding quarter and year
            quarter_year_split = column_headers[index].split(' ')
            quarter = quarter_year_split[0].lower()
            year = quarter_year_split[1].lower()
            
            # add all data to course object
            if self.year == -1:
                self.year = year
            
            # if days is None need to adjust 
            if days is None:
                return
            
            for day in days:
                for time in times:
                    timespan = time_span.TimeSpan()
                    timespan.parse_time(time)
                    self.add_time_to_day(quarter, day, timespan)


    def __str__(self):
        result = f'{self.course_id} {self.title}\n{self.year}\n'
        
        # Iterate over the quarters and add their information
        for quarter, days in self.quarter_to_days.items():
            result += f'{quarter.capitalize()}: '
            
            if not days:
                # If no days are scheduled for this quarter
                result += 'No classes offered\n'
                continue
            
            quarter_info = []
            for day, times in days.items():
                if times:
                    # Convert each TimeSpan object to its string representation
                    times_str = ', '.join(str(time) for time in times)
                    quarter_info.append(f'{day}: {times_str}')
                else:
                    # If no times are specified for this day
                    quarter_info.append(f'{day}: No times specified')
            
            if quarter_info:
                # Join all day information with a separator for readability
                result += ' | '.join(quarter_info) + '\n'
            else:
                # If the days dictionary exists but has no entries
                result += 'No classes offered\n'
        
        return result


            

