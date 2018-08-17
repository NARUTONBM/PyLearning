#! python3
# rename_dates.py - Renames fileNames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# 创建一个匹配美式时间的正则表达式
dateRegex = re.compile(r"""^(.*?)   # 日期前的所有内容
    (([01])?\d)-                    # 一或两个数字匹配月份
    (([0123])?\d)-                  # 一或两个数字匹配日期
    ((19|20)\d\d)                   # 四个数字匹配时间
    (.*?)$                          # 日期后的所有文本
    """, re.VERBOSE)

# 循环遍历工作文件夹的所有文件
for amerFileName in os.listdir('.'):
    regexResult = dateRegex.search(amerFileName)

    # 忽略没有日期的文件
    if regexResult is None:
        continue

    # 获取文件名的不同部分
    beforePart = regexResult.groups(1)
    monthPart = regexResult.groups(2)
    dayPart = regexResult.groups(4)
    yearPart = regexResult.groups(6)
    afterPart = regexResult.groups(8)

    # 组合成欧洲时间风格的文件名
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # 获取完整的绝对路径
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # 重命名文件
    print('重命名 \n%s\nto%s' % (amerFileName, euroFileName))
    shutil.move(amerFileName, euroFileName)
