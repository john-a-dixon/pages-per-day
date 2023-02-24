import sys
from datetime import datetime



def is_leap(year):
    return ((year % 4) == 0 & (year % 100) != 0) | (year % 400) == 0 

def pages_per_day(pages, days):
    pass

def full_year():
    year = datetime.now().year
    day_count = int(datetime.now().strftime("%j"))
    if(is_leap(year) and day_count == 60):
        print('No reading today')
    elif(day_count < 86):
        day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
        print(f'Page {day_count * 4}')
    else:
        day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
        print(f'Page: {(85 * 4) + ((day_count - 85) * 3)}')


def duration_of_days(num_days):
    pass

full_year()