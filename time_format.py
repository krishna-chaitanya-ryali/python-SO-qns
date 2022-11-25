#how to customize the time format 
#i'm tring to insert 0 if hours are in single number(04) or if hours are in 24hours format then it should not be changed. I'm new to python. plz guide me.

# current_time = '08:00'
# lst = ['00:00','04:00','08:00','12:00','16:00','20:00']
# if current_time in lst:
#     hour, minute = current_time.split(':')
#     if hour == '00':
#         hour = '24'
#     start_hour = int(hour)-4
#     start_time = str(start_hour)+':'+'00'
#     end_hour = int(hour)-1
#     end_time = str(end_hour)+':'+'59'
#     print(start_time,end_time)


#I'm getting output like this:

#4:00 7:59

#but I'm expecting output like this

#04:00 07:59
#==================================

#solution 1

current_time = '08:00'
lst = ['00:00','04:00','08:00','12:00','16:00','20:00']
if current_time in lst:
    hour, minute = current_time.split(':')
    if hour == '00':
        hour = '24'
    start_hour = int(hour)-4
    start_time = str(start_hour).zfill(2)+':'+'00'
    end_hour = int(hour)-1
    end_time = str(end_hour).zfill(2)+':'+'59'
    print(start_time,end_time)

#Result:

#04:00 07:59