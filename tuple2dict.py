#I've trying to convert list of tuples to customized dictionaries. I'm trying to divide pack owner, submitter and consumer

lst = [('name1', 'email1','id1','new1',11,'1','po'),
       ('name2', 'email2','id2','new2',12,'2','sub'),
       ('name3', 'email3','id3','new3',13,'3','sub'),
       ('name4', 'email4','id4','new4',14,'4','po'),
       ('name5', 'email5','id5','new5',15,'5','cons')]



#Expected Output

{
"add_sub":{
"sub":[{"id":"id2","name":"name2","email":"email2"},{"id":"id3","name":"name3","email":"email3"}],
"po":[{"id":"id1","name":"name1","email":"email1"},{"id":"id4","name":"name4","email":"email4"}],
"consumer":[{"id":"id5","name":"name5","email":"email5"}]},}

#======================================================


#working solution
#collections.defaultdict to the rescue:

from collections import defaultdict

lst = [('name1', 'email1', 'psid1', 'new1', 11, '1', 'pack owner'),
       ('name2', 'email2', 'psid2', 'new2', 12, '2', 'submitter'),
       ('name3', 'email3', 'psid3', 'new3', 13, '3', 'submitter'),
       ('name4', 'email4', 'psid4', 'new4', 14, '4', 'pack owner'),
       ('name5', 'email5', 'psid5', 'new5', 15, '5', 'consumer')]

by_role = defaultdict(list)

for name, email, psid, new, id1, id2, role_name in lst:
    by_role[role_name].append({"name": name, "email": email, "psid": psid})

print({"add_sub": dict(by_role)})

#output

{'add_sub': 
  {'pack owner': [{'name': 'name1', 'email': 'email1', 'psid': 'psid1'}, {'name': 'name4', 'email': 'email4', 'psid': 'psid4'}],
   'submitter': [{'name': 'name2', 'email': 'email2', 'psid': 'psid2'}, {'name': 'name3', 'email': 'email3', 'psid': 'psid3'}],
   'consumer': [{'name': 'name5', 'email': 'email5', 'psid': 'psid5'}]
  }
}

#==========================================================================
#other answers

res = {"add_sub":{}}
for name, mail, psid, *_, role_name in lst:
    res['add_sub'].setdefault(role_name, []).append({"name":name, "email":mail, "psid":psid})

{'add_sub': 
  {'consumer': [{'email': 'email5', 'name': 'name5', 'psid': 'psid5'}],
  'pack owner': [{'email': 'email1', 'name': 'name1', 'psid': 'psid1'},
                 {'email': 'email4', 'name': 'name4', 'psid': 'psid4'}],
  'submitter': [{'email': 'email2', 'name': 'name2', 'psid': 'psid2'},
                {'email': 'email3', 'name': 'name3', 'psid': 'psid3'}]}}