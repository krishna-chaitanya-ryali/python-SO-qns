#How to sort list of dictionaries of dates its value

#I'm trying to sort the values with current year.

mdlist = [{0:'31 Jan 2022', 1:'', 2:'10 Feb 2022'},
          {0:'10 Feb 2021', 1:'20, Feb 2021', 2:''}, 
          {0:'10 Feb 2022', 1:'10 Feb 2022', 2:'10 Feb 2022'}]

#Expected output

mdlist_out = [{0:'31 Jan 2022', 1:'', 2:'10 Feb 2022'},
          {0:'10 Feb 2022', 1:'10 Feb 2022', 2:'10 Feb 2022'},
          {0:'10 Feb 2021', 1:'20 Feb 2021', 2:''}]


#solution 1

#Maybe you could leverage the fact that these are datetimes by using the datetime module and sort it by the years in descending order and the month-days in ascending order:

from datetime import datetime
def sorting_key(dct):
    ymd = datetime.strptime(dct[0], "%d %b %Y")
    print(-ymd.year, ymd.month, ymd.day)

mdlist.sort(key=sorting_key)

#Output:

# mdlist = [{0: '31 Jan 2022', 1: '', 2: '10 Feb 2022'},
#  {0: '10 Feb 2022', 1: '10 Feb 2022', 2: '10 Feb 2022'},
#  {0: '10 Feb 2021', 1: '20 Feb 2021', 2: ''}]


 #================================================================

 #solution 2

#Use a key function that returns 0 if the year is 2022, 1 otherwise. This will sort all the 2022 dates first.

firstyear = '2022'
mdlist = sorted(mdlist, key=lambda d: 0 if d:d[0].split()[-1] == firstyear else 1)
