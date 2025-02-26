import os, shutil
from shutil import copyfile
cwd = os.getcwd()
print(cwd)
newList=[]
#from shutil import copyfile
imgs=['0H0A0109.JPG', '0H0A0181.JPG', 'CCD_3111.JPG', 'CCD_3127.JPG', 'CCD_3162.JPG', 'CCD_3341.JPG', 'CCD_3349.JPG', 'CCD_3391.JPG', 'CCD_3404.JPG', 'CCD_3461.JPG', 'CCD_3664.JPG', 'CCD_3727.JPG', 'CCD_3813.JPG', 'CCD_3889.JPG', 'CCD_3954.JPG', 'CCD_3983.JPG', 'CCD_4029.JPG', 'CCD_4093.JPG', 'CCD_4124.JPG', 'CCD_4205.JPG', 'CCD_6383.JPG', 'CCD_6644.JPG', 'CCD_6800.JPG', 'CCD_6835.JPG', 'CCD_7029.JPG', 'CCD_7120.JPG', 'CCD_7145.JPG', 'DSC_2409.JPG', 'DSC_2428.JPG', 'DSC_3628.JPG', 'DSC_3738.JPG']
dest_folder = r'I:\30Photos'
src=r"I:\MAIN FILES"
newLst=[]
count = 0
#os.mkdir('F:\my_new_folder')
for root, dirs, files in os.walk(src):
  for file in files:
      #print(file)
      if file in imgs:
          print(file)
          count+=1
          totalCopyPath = os.path.join(root, file)
          print(totalCopyPath)
          shutil.copy(totalCopyPath, dest_folder)
      else:
          test=str(file)
          newLst.append(test)
print(count)
print(newLst)