import datetime

current_date = datetime.datetime.now()
print(f"Current Date and Time: {current_date}")

current_date = datetime.date.today
print(f"Current Date: {current_date}")

current_time = datetime.datetime.now().time()
print(f"Current Time: {current_time}")

specific_time = datetime.time(14, 35, 12)
print(f"Specific Time: {specific_time}")

formatted_datetime = current_time.strftime("%A, %B %d, %Y %H:%M:%S")
print(f"Formatted Date and Time: {formatted_datetime}")

date_string = "2024-11-23 14:35:12"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:S") #%H is millitary time and %I for 12hr clock
print(f"Parsed Date and time: {parsed_datetime}")

new_date = current_date + datetime.timedelta(days=7)
print(f"New date (7 days later): {new_date}")

earlier_date = current_date - datetime.timedelta(days=7)
print(f"Earlier date (7 days ago): {earlier_date}")

weekday = current_date.weekday()

print(f"Day of the Week (0=Monday, 6=Sunday): {weekday}")

# 11. Get the number of days in a month (using date's `monthrange` function)

import calendar

days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]

print(f"Days in current month: {days_in_month}")
