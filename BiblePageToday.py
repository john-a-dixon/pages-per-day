from datetime import datetime

year = datetime.now().year
day_count = int(datetime.now().strftime("%j"))
is_leap = year % 4 == 0


if(is_leap and day_count == 60):
    print('No reading today')
elif(day_count < 86):
    day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    print(f'Page {day_count * 4}')
else:
    day_count = day_count - 1 if (is_leap and day_count > 60) else day_count
    print(f'Page: {(85 * 4) + ((day_count - 85) * 3)}')