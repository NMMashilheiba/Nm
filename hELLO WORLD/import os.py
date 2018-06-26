import os
from string import digits
list_file=os.listdir("C:\\Users\\NM M M\\Desktop\\Quora pics\\prank dir\\prank")
#print(list_file)
os.chdir("C:\\Users\\NM M M\\Desktop\\Quora pics\\prank dir\\prank")
#
for file in list_file:
    #get oldname of file
    old_name = file
    print (old_name)
    #newname of file = oldname-number
    new_name = old_name.lstrip(digits)
    print (new_name)
    #rename the file (oldname,newname)
    os.rename(old_name,new_name)