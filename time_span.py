
class TimeSpan:

    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int

    def __init__(self, start_hour=0, start_minute=0, end_hour=0, end_minute=0):
        ''' 
        Manually input the start and end times for the span. Does not convert to military time,
        so start_hour must be <= end_hour
        '''
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute

        self.validate()


    def parse_time(self, time_string):
        '''
        Given a string representing the start and end times of a class, 
        parse the string, initialize object, and convert to military time.
        Validates input format and checks for invalid times.
        '''
        try:
            # Split the time string by '-'
            times = time_string.split('-')
            
            if len(times) != 2:
                raise ValueError(f"Time string '{time_string}' must be of the format H(H)(:MM)-H(H)(:MM)'")
            
            # Split start and end times by ':'
            start_time = times[0].strip().split(':')
            end_time = times[1].strip().split(':')
            
            # Parse hours and minutes, validate format
            if not (1 <= len(start_time) <= 2) or not (1 <= len(end_time) <= 2):
                raise ValueError(f"Invalid time format in '{time_string}'")

            # Convert start and end hours and minutes to integers
            self.start_hour = int(start_time[0])
            self.end_hour = int(end_time[0])
            
            self.start_minute = 0
            if len(start_time) > 1:
                self.start_minute = int(start_time[1])

            self.end_minute = 0
            if len(end_time) > 1:
                self.end_minute = int(end_time[1])
            
            # Additional validation for valid time ranges
            if not (0 <= self.start_hour <= 23) or not (0 <= self.end_hour <= 23):
                self.start_hour = 0
                self.end_hour = 0
                raise ValueError(f"Hours must be between 0 and 23 in '{time_string}. Setting hours to 0.'")
            if not (0 <= self.start_minute <= 59) or not (0 <= self.end_minute <= 59):
                self.start_minute = 0
                self.end_minute = 0
                raise ValueError(f"Minutes must be between 0 and 59 in '{time_string}. Setting minutes to 0.'")
            
            # Convert to military time
            self.to_military()

        except ValueError as ve:
            print(f"Error parsing time string: {ve}")
            raise  # Optionally re-raise the exception for further handling



    # compute the length of the TimeSpan, in minutes
    @property
    def duration(self) -> int:
        return (self.end_hour - self.start_hour) * 60 + (self.end_minute - self.start_minute)


    def validate(self):
        # start and end must be between 0 - 23 for hours, 0 - 59 for minutes

        if self.start_hour < 0 or self.start_hour > 23:
            raise ValueError(f'start_hour must be between 0 - 23: {self.start_hour}')
        if self.start_minute < 0 or self.start_minute > 59:
            raise ValueError(f'start_minute must be between 0 - 59 {self.start_minute}')
        if self.end_hour < 0 or self.end_hour > 23:
            raise ValueError(f'end_hour must be between 0 - 23: {self.end_hour}')
        if self.end_minute < 0 or self.end_minute > 59:
            raise ValueError(f'end_minute must be between 0 - 59 {self.end_minute}')
        
        # end cannot be before start
        if self.end_hour < self.start_hour:
            raise ValueError(f'end hour {self.end_hour} must be later than start: {self.start_hour}')
        if self.end_hour == self.start_hour:
            if self.end_minute < self.start_minute:
                raise ValueError(f'class starts and ends in the same hour. end minute {self.end_minute} must be later than start minute: {self.start_minute}')
    
    def to_military(self):
        '''
        This is a particular function because it only converts times in a specific range. 
        On the CS page, it is assumed that if a class is before 8:00, it must be in the afternoon. '''
        if self.start_hour < 8:
            self.start_hour += 12
            self.end_hour += 12
            return
        
        # if the span goes across noon, the end time must be adjusted 
        if self.start_hour < 12 and self.end_hour < 12 and self.end_hour < self.start_hour:
            self.end_hour += 12

    def print_raw(self):
        print(f'{self.start_hour}:{self.start_minute} - {self.end_hour}:{self.end_minute}')
        
