#! python3
# clean_dir.py

import os

for folderName, subFolders, fileNames in os.walk(input('请输入您要清理的文件目录：')):
    for file in fileNames:
        if os.path.getsize(os.path.join(folderName, file)) > 1024 * 1024:
            print(os.path.join(folderName, file))

