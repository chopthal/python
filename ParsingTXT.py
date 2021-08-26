import os
import pandas as pd
# import webbrowser

knownProtocolList = [
    '36 31 30 31 31 30 30 31',
    '36 31 30 31 35 31 30 35'
]

pathName = ''
fileName = 'log'
fileExt = 'txt'
resultFileName = fileName + '_result'
fullFile = os.path.join(pathName, fileName+'.'+fileExt)
resultFullFile = os.path.join(pathName, resultFileName+'.'+fileExt)

with open(fullFile, 'r', encoding='utf-16') as f:
    lines = f.readlines()

    # print(len(lines))
    result = list()

    for i, line in enumerate(lines):
        if ' 02 ' in line[0:5]:
            extractedLine = line[0:line.find('.')]
            result.append(extractedLine[extractedLine.find(
                '02'):extractedLine.find('03')+2])
            # print(len(result))

# print(len(result))
uniqResult = list()

# print(knownProtocolList[0])

for line in result:
    if line not in uniqResult:
        uniqResult.append(line)

delList = list()
for i, line in enumerate(uniqResult):
    for knownProtocol in knownProtocolList:
        if knownProtocol in line:
            delList.append(i)

# print(delList)

unknownProtocol = list()
for i, line in enumerate(uniqResult):
    if i not in delList:
        unknownProtocol.append(line)

protocol = "\n".join(unknownProtocol)
print(protocol)

with open(resultFullFile, 'w', encoding='utf-8') as f:
    f.writelines(protocol)

# webbrowser.open(resultFullFile)
