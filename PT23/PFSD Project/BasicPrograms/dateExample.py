import datetime
import time
import calendar
from datetime import datetime
import pytz

# # # Time
# # print(time.time())
# # print(time.asctime())
# #
# # # Date and Time
# # datetime_object = datetime.datetime.now()
# # print(datetime_object)
# # print("Year: ", datetime_object.year)
# # print("Month: ", datetime_object.month)
# # print("Day: ", datetime_object.day)
# # print("Hour: ", datetime_object.hour)
# # print("Minute: ", datetime_object.minute)
# # print("Second: ", datetime_object.second)
# #
# # # Calendar
# # calendar.prcal(2023)
# # s2 = calendar.month(2024, 12)
# # print(s2)
# # s3 = calendar.isleap(2018)
# # print(f"2018 isleap: {s3}")

from datetime import timedelta

n = int(input("Enter number of days: "))
print(datetime.datetime.now() + timedelta(days=n))

# time1 = pytz.timezone('America/Los_Angeles')
# print("Current time in Los Angeles, America is: ", datetime.now(time1))
#
# time1 = pytz.timezone('Europe/Berlin')
# print("Current time in Berlin, Europe is: ", datetime.now(time1))
#
# time1 = pytz.timezone('Asia/Karachi')
# print("Current time in Karachi, Pakistan is: ", datetime.now(time1))