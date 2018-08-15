#! Python3
# mad_libs.py - 将读入文本文件，并让用户在该文本文件中出现 ADJECTIVE、NOUN、ADVERB 或 VERB 等单词的地方，加上他们自己的文本。

import os, re

baseFilePath = os.getcwd() + '\mad_libs_b.txt'
outputFilePath = os.getcwd() + '\mad_libs_o.txt'
baseContent = r'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

dirName = os.path.dirname(baseFilePath)
if not os.path.exists(dirName):
    os.mkdir(dirName)
    baseFile = open(baseFilePath, 'a')
    baseFileRead = baseContent
else:
    if not os.path.exists(baseFilePath):
        baseFile = open(baseFilePath, 'a')
        baseFileRead = baseContent
    else:
        baseFile = open(baseFilePath, 'r')
        baseFileRead = baseFile.read()
        if baseFileRead == '':
            baseFileRead = baseContent

baseFile.close()

toRepList = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
for repItem in toRepList:
    inputItem = input('Enter an ' + repItem + ':\n')
    regexWord = re.compile(repItem)
    baseFileRead = regexWord.sub(inputItem, baseFileRead)

outputFile = open(outputFilePath, 'w')
outputFile.write(baseFileRead)
outputFile.close()

print('Your sentence:\n' + baseFileRead)
