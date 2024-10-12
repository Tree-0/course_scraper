'''
Module providing an object to represent university classes, and methods to add, edit, 
and remove information about those classes
'''
class Course:
    '''
    Represents one university course, containing information about the name and id of the course,
    as well as what quarters, days, and times the course is offered. 
    '''
    def __init__(self, course_id, title):
        self.id = course_id # course category and number e.g. COMP_SCI 150
        self.title = title # title e.g. Intro to Computer Science

        # Each course will be offered a number of quarters
        # Each quarter will have classes offered on certain days
        # Each day will have classes offered at a certain time
        # By default, object is created with no classes ever offered
        self.quarter_to_days = {'fall':None, 'winter':None, 'spring':None, 'summer':None}

        # Each day will have class offered at a certain time
        # By default, class will never be offered. No class on weekends

        ''' 
        Here is what each value in quarter_to_days should look like: 
        '''
        # day_to_times = {'M':None, 'Tu':None, 'W':None, 'Th':None, 'F':None}

        # Each value in day_to_times should be an instance of TimeSpan

        # TimeSpan(start_hr, start_mnt, end_hr, end_mnt)

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
        given a quarter (str), a day (str), and a time (TimeSpan), add the offered time to the course object
        '''

        # if no times have been added to the day, create empty dict
        if self.quarter_to_days[quarter][day] is None:
            self.quarter_to_days[quarter][day] = {}
    
        # add the time to the day
        self.quarter_to_days[quarter][day].append(time)
