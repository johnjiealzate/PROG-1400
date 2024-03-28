# It imports necessary modules: datetime for working with dates and times, and timedelta to represent differences in datetime values.
from datetime import datetime, timedelta
# Decimal time represents seconds since the Unix epoch (January 1, 1970), while the offset is the time zone difference in seconds from UTC
decimal_time = 1711629855
decimal_time_offset = -10800 # Halifax
epoch = datetime(1970, 1, 1)  # Unix epoch (January 1, 1970)
timestamp = epoch + timedelta(seconds=decimal_time)
# Un-comment for Troubleshooting
#print(f"{timestamp}")
current_time = timestamp + timedelta(seconds=decimal_time_offset)
# Un-comment for Troubleshooting
# print(f"{current_time.day}")
# print(f"{current_time.month}")
# print(f"{current_time.year}")
weekday = current_time.strftime("%A")
print(f"{current_time.strftime("%A %m-%d-%Y %H:%M:%S")}")
print(f"{current_time.strftime("%A %B %d, %Y %H:%H")}")
print(f"{current_time.strftime("%a %b %d, %Y %H:%H %p")}")
