#trying to customize the python nested dictionaries
#I've trying to convert list to tuples to customized list to dictionaries. I'm able toto divide admin, pack owner, submitter, consumer and read only. Please check below code and output

#expected question

from collections import defaultdict

role_details = ['po','sub', 'cons', 'admin','read']

lst = [('name1', 'email1', 'psid1', 'new1', 11, '1', 'po'),
       ('name2', 'email2', 'psid2', 'new2', 12, '2', 'sub'),
       ('name3', 'email3', 'psid3', 'new3', 13, '3', 'sub'),
       ('name4', 'email4', 'psid4', 'new4', 14, '4', 'po'),
       ('name5', 'email5', 'psid5', 'new5', 15, '5', 'cons')]

by_role = defaultdict(list)

for name, email, psid, new, id1, id2, role_name in lst:
    by_role[role_name].append({"name": name, "email": email, "psid": psid})

print({"add_sub": dict(by_role)})



{'add_sub': 
  {'po': [{'name': 'name1', 'email': 'email1', 'psid': 'psid1'}, {'name': 'name4', 'email': 'email4', 'psid': 'psid4'}],
   'sub': [{'name': 'name2', 'email': 'email2', 'psid': 'psid2'}, {'name': 'name3', 'email': 'email3', 'psid': 'psid3'}],
   'cons': [{'name': 'name5', 'email': 'email5', 'psid': 'psid5'}]
  }
}

#expected output

{'add_sub':
  {'admin': [], 
  'po': [{'name': 'name1', 'email': 'email1', 'psid': 'psid1'}, {'name': 'name4', 'email': 'email4', 'psid': 'psid4'}],
  'read': [],
   'sub': [{'name': 'name2', 'email': 'email2', 'psid': 'psid2'}, {'name': 'name3', 'email': 'email3', 'psid': 'psid3'}],
   'cons': [{'name': 'name5', 'email': 'email5', 'psid': 'psid5'}]
  }
}

#original answer working solution

#You can also create the dict with all the keys you need beforehand. In this case you don't even need the defaultdict, unless you need its functionality later.

#from collections import defaultdict

role_details = ['pack owner','submitter', 'consumer', 'admin','read only']

lst = [('name1', 'email1', 'psid1', 'new1', 11, '1', 'pack owner'),
       ('name2', 'email2', 'psid2', 'new2', 12, '2', 'submitter'),
       ('name3', 'email3', 'psid3', 'new3', 13, '3', 'submitter'),
       ('name4', 'email4', 'psid4', 'new4', 14, '4', 'pack owner'),
       ('name5', 'email5', 'psid5', 'new5', 15, '5', 'consumer')]

#by_role = defaultdict(list)
by_role = {k: [] for k in role_details}

for name, email, psid, new, id1, id2, role_name in lst:
    by_role[role_name].append({"name": name, "email": email, "psid": psid})

print({"add_sub": by_role})

#output

{'add_sub': 
   {'pack owner': [{'name': 'name1', 'email': 'email1', 'psid': 'psid1'}, {'name': 'name4', 'email': 'email4', 'psid': 'psid4'}], 
   'submitter': [{'name': 'name2', 'email': 'email2', 'psid': 'psid2'}, {'name': 'name3', 'email': 'email3', 'psid': 'psid3'}], 
   'consumer': [{'name': 'name5', 'email': 'email5', 'psid': 'psid5'}], 
   'admin': [], 
   'read only': []}
}

#Also note that you don't need the dict() call in the print, since by_role is already a dict

#If you do need the defaultdict, you can do the same thing with this line:

from collections import defaultdict

# ...code...

by_role = defaultdict(list, {k: [] for k in role_details})

#next answer

#by_role is a defaultdict(list), so you'll get an empty list if you try to access the by_role['admin'] or by_role['read only'].

#In fact, all you need to do is try to access those keys once, and they get added to the defaultdict, so you can iterate over role_details and do that:

for name, email, psid, new, id1, id2, role_name in lst:
    by_role[role_name].append({"name": name, "email": email, "psid": psid})

for role_name in role_details:
   _ = by_role[role_name] # Try to access every key, and don't do anything with it.


{'add_sub': {
    'pack owner': [
         {'name': 'name1', 'email': 'email1', 'psid': 'psid1'},
         {'name': 'name4', 'email': 'email4', 'psid': 'psid4'}
     ],
    'submitter': [
         {'name': 'name2', 'email': 'email2', 'psid': 'psid2'},
         {'name': 'name3', 'email': 'email3', 'psid': 'psid3'}
     ],
    'consumer': [{'name': 'name5', 'email': 'email5', 'psid': 'psid5'}],
    'admin': [],
    'read only': []
   }
}