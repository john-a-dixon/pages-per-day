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

    print(days_to_count)
    print(first_portion, second_portion)

    # if(is_leap(year) and day_count == 60):
    #     print('No reading today')
    # elif(day_count <= first_portion[0]):
    #     day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    #     print(f'Page {day_count * 4}')
    # else:
    #     day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    #     print(f'Page: {(85 * 4) + ((day_count - 85) * 3)}')


def duration_of_days(num_days):
    pass

full_year()
# print(pages_per_day(1180, 365))