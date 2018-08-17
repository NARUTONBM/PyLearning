#! python3
# backup_to_zip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os


# 备份folder文件夹下所有的内容到zip文件中
def backup_to_zip(folder):
    # 确认folder是绝对路径
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break

        number += 1

    # 创建zip文件
    print('正在创建Zip文件：%s' % zip_file_name)
    backup_zip_file = zipfile.ZipFile(zip_file_name, 'w')

    # 遍历目录树，并添加到ZIP文件
    for folderName, subFolders, fileNames in os.walk(folder):
        print('添加文件%s' % folderName)
        # 添加当前文件夹到zip文件
        backup_zip_file.write(folderName)

        # 添加文件夹下所有的文件到ZIP文件
        for fileName in fileNames:
            if fileName.startswith(os.path.basename(folder) + '_') and fileName.endswith('.zip'):
                continue
            backup_zip_file.write(os.path.join(folderName, fileName))

    backup_zip_file.close()
    print('完成')


backup_to_zip('c:\\delicious')
