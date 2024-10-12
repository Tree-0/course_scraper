from dataclasses import dataclass

@dataclass
class TimeSpan:
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    
    # compute the length of the TimeSpan, in minutes
    @property
    def duration(self) -> int:
        return (self.end_hour - self.start_hour) * 60 + (self.end_minute - self.start_minute)


    def __post_init__(self):
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
        
