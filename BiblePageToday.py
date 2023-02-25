import sys
from datetime import datetime



def is_leap(year):
    return ((year % 4) == 0 & (year % 100) != 0) | (year % 400) == 0 

def pages_per_day(pages, days):
    num_pages = int(pages / days)
    days_reading_one_extra_page = pages % days
    return (days_reading_one_extra_page, num_pages + 1), (days - days_reading_one_extra_page, num_pages)

def full_year():
    first_portion, second_portion = pages_per_day(int(sys.argv[1]), 365)
    # The current year
    year = datetime.now().year
    # The current day of the year
    day_count = int(datetime.now().strftime("%j"))
    # The days to use when calculating the number of pages. Since leap years are not counted, this is important
    days_to_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    

    if(is_leap(year) and day_count == 60):
        print('No reading today')
    elif(days_to_count <= first_portion[0]):
        print(f'Read to the end of page {days_to_count * first_portion[1]}')
    else:
        print(f'Page: {(first_portion[0] * first_portion[1]) + ((days_to_count - first_portion[0]) * second_portion[1])}')


if len(sys.argv) == 2:
    full_year()
else:
    print(pages_per_day(int(sys.argv[1]), int(sys.argv[2])))
