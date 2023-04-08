import os
import shutil

from_dir = "C:/Users/Aashima Bandiwadekar/Downloads"
to_dir = "C:/Users/Aashima Bandiwadekar/Downloads/Document_File"

list_files = os.listdir(from_dir)
print(list_files)

for file in list_files:
    name,extension = os.path.splitext(file)
    print("Name of "+file +" is "+name)
    print("Extension of "+file +" is "+extension)
    print()