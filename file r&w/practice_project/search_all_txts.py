#! Python3
# search_all_txts.py - 打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。

import os, re, sys

cwd = os.getcwd()
txtDirList = []

# 查找匹配的文件
regex1 = re.compile(r'\.txt')
for x in os.listdir(cwd):
    if regex1.search(x):
        txtDirList.append(x)
print(txtDirList)

# 根据传入的参数来匹配需要行
regex2 = re.compile(input('Enter your regex'))
txtLineList = []
for x in txtDirList:
    with open(x, 'r', encoding='UTF-8')as txtFile:
        txtLineList = txtFile.readline()
        for y in txtLineList:
            if regex2.search(y):
                print(y + '\n')
