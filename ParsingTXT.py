import os
# import pandas as pd
# import webbrowser

def FindUnknownProtocolList(knownProtocolList, inputPathName, inputFileName, savePathName='', saveFileName='result', fileExt='txt'):

    fullFile = os.path.join(inputPathName, inputFileName+'.'+fileExt)
    resultFullFile = os.path.join(savePathName, saveFileName+'.'+fileExt)

    with open(fullFile, 'r', encoding='utf-16') as f:
        lines = f.readlines()
        result = list()
        for i, line in enumerate(lines):
            if ' 02 ' in line[0:5]:
                extractedLine = line[0:line.find('.')]
                result.append(extractedLine[extractedLine.find(
                    '02'):extractedLine.find('03')+2])

    uniqResult = list()

    for line in result:
        if line not in uniqResult:
            uniqResult.append(line)

    delList = list()
    for i, line in enumerate(uniqResult):
        for knownProtocol in knownProtocolList:
            if knownProtocol in line:
                delList.append(i)

    unknownProtocol = list()
    for i, line in enumerate(uniqResult):
        if i not in delList:
            unknownProtocol.append(line)

    protocol = "\n".join(unknownProtocol)
    print(protocol)

    with open(resultFullFile, 'w', encoding='utf-8') as f:
        f.writelines(protocol)


knownProtocolList = [
    '36 31 30 31 31 30 30 31',
    '36 31 30 31 35 31 30 35'
]

pathName = ''
fileName = 'log'

FindUnknownProtocolList(knownProtocolList, pathName, inputFileName=fileName, savePathName='', saveFileName='log_result2', fileExt='txt')