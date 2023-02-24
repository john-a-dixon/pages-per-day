import datetime
import matplotlib

day_of_year = datetime.datetime.now().timetuple()
day_count = day_of_year.tm_yday
year = day_of_year.tm_year
is_leap = year % 4 == 0

if(is_leap and day_count == 60):
    print('No reading today')
elif(day_count < 86):
    day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    print(f'Page {day_count * 4}')
else:
    day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    print(f'Page: {(85 * 4) + ((day_count - 85) * 3)}')