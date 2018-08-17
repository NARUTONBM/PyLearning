#! python3
# selective_copy.py

import os, shutil

os.chdir(input('输入你希望此脚本工作的目录：'))

copy_file_name = 'copy_dir'
try:
    os.makedirs(copy_file_name)
except FileExistsError:
    pass

for folderName, subFolders, fileNames in os.walk('.'):
    for file in fileNames:
        if file.endswith('.pdf') or file.endswith('.jpg'):
            if file not in os.listdir(copy_file_name):
                shutil.copy(os.path.join(folderName, file), copy_file_name)
