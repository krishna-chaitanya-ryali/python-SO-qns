# how to remove the duplicate key and values in list of dictionaries and append unique list of values to a key

list_of_dict=[{'f_text':'sample', 'symbol':'*', 'f_id':246, 'record_id':'4679', 'flag': 'N'},
{'f_text':'sample', 'symbol':'*', 'f_id':246, 'record_id':'4680', 'flag': 'N'},
{'f_text':'other text', 'symbol':'!#', 'f_id':247, 'record_id':'4678', 'flag': 'N'}]

#In the above list of dictionaries the first and second lines has same 'f_id':'246'. 
#so I'm trying to remove duplicate key and values in the dictionary and make 'record_id':['4679','4680'].

#I'm expecting the below output

# [{'f_text':'sample', 'symbol':'*', 'f_id':246, 'record_id':['4679',4680], 'flag': 'N'},
# {'f_text':'other text', 'symbol':'!#', 'f_id':247, 'record_id':'4678', 'flag': 'N'}]

#@U12-Forward's answer works only if the input is pre-sorted, with records of the same f_ids already grouped together.
#A better-rounded approach that works regardless of the order of the input would be to build a dict that maps f_ids to respective dicts, 
#but convert the record_id value to a list when there are multiple records with the same f_ids:

mapping = {}
for d in list_of_dict:
    try:
        entry = mapping[d['f_id']] # raises KeyError
        entry['record_id'].append(d['record_id']) # raises AttributeError
    except KeyError:
        mapping[d['f_id']] = d
    except AttributeError:
        entry['record_id'] = [entry['record_id'], d['record_id']]
print(list(mapping.values()))

#output:

#[{'f_text': 'sample', 'symbol': '*', 'f_id': 246, 'record_id': ['4679', '4680'], 'flag': 'N'}, 
#{'f_text': 'other text', 'symbol': '!#', 'f_id': 247, 'record_id': '4678', 'flag': 'N'}]