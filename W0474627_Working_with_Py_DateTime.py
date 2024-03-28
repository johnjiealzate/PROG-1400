# It imports necessary modules: datetime for working with date and times, and timedelta
from datetime import datetime, timedelta

decimal_time = 1711057460
decimal_time_offset = -10800 # Halifax
epoch = datetime(1970,1,1) # Unix epoch
timestamp = epoch + timedelta(seconds=decimal_time)
print(f"{timestamp}")
current_time = timestamp + timedelta(seconds=decimal_time_offset)
print(f'{current_time.day}')
print(f"{current_time.month}")
print(f"{current_time.year}")


