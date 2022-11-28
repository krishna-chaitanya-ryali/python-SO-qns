# how to replace date and time in datetime object.

# I'm trying to pass dynamically hours and minutes to the time_now variable.

# I want to pass time dynamically to time_now. I'm trying but unable to pass it.

from datetime import datetime

# split your time to be usable with replace
new_time = '16:50'
hour, minute = new_time.split(':')

# it's not mandatory if date_time is already a datetime instance
date_time = '2022-02-10 14:18:58.209240+05:45'
date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f%z')

# replace each component with keyword args
new_time = date_time.replace(hour=int(hour), minute=int(minute))

print(str(new_time))

#output

# str(new_time)
# '2022-02-10 16:50:58.209240+05:45'