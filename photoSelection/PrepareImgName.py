from config import str
final = []
lines_list = str.splitlines()
for each in lines_list:
    new_str = 'IMG_'+each +'.HEIC'
    final.append(new_str)
print(final)
print(len(final))