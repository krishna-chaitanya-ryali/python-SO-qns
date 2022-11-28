#Below is my list of dictionaries:

#I'm tried to remove the duplicate values from 'r_id'. some values are in list and some are in string.

list_of_dict = [{'fid':200, 'r_id':['4321', '4321']}, {'fid':201, 'r_id':'5321'}]

#expected output

list_of_dict = [{'fid':200, 'r_id':['4321']}, {'fid':201, 'r_id':['5321']}]

#solution 1 

#If in item['r_id'] you have another type like str you can try this:


list_of_dict = [{'fid':201, 'r_id':'5321'}, {'fid':200, 'r_id':['4321', '4321']}]

for item in list_of_dict:
    if type (item['r_id']) == list:
  # if isinstance(item['r_id'],list):
        item['r_id'] = list(set(item['r_id']))
    elif type (item['r_id']) == str:
  # elif isinstance(item['r_id'],str):
         item['r_id'] = [item['r_id']]


print(list_of_dict)

#solution 2

#Shortest approach
# >>> [{'fid' : item['fid'], 'r_id' : list(set(item['r_id'])) if type(item['r_id']) == list else [item['r_id']]} for item in list_of_dict]

# [{'fid': 201, 'r_id': ['5321']}, {'fid': 200, 'r_id': ['4321']}]
