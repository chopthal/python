import os
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def read_pdf_PDFMINER(pdf_file_path):    
    
    # pdf_file_path = 'path/xxx.pdf'
    
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())


def save_string_to_text(inputString, savePathName='', saveFileName='result'):    

    resultFileExt = 'txt'
    resultFileName = saveFileName
    resultFullFile = os.path.join(savePathName, resultFileName +'.'+ resultFileExt)

    with open(resultFullFile, 'w', encoding='utf-8') as f:
        f.writelines(inputString)


def FindUnknownProtocolList(inputPathName, inputFileName, knownProtocolList=None, savePathName='', saveFileName='result', fileExt='txt'):

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

    # Remove duplicates    
    uniqResult = list()

    for line in result:
        if line not in uniqResult:
            uniqResult.append(line)

    delList = list()
    if knownProtocolList != None:
        for i, line in enumerate(uniqResult):
            for knownProtocol in knownProtocolList:
                if knownProtocol in line:
                    delList.append(i)
                    
    unknownProtocol = list()
    for i, line in enumerate(uniqResult):
        if i not in delList:
            unknownProtocol.append(line)

    protocolList = "\n".join(unknownProtocol)

    with open(resultFullFile, 'w', encoding='utf-8') as f:
        f.writelines(protocolList)
        
    return protocolList


pathName = ''
fileName = 'sample'
fileExt = 'pdf'
fullFile = os.path.join(pathName, fileName+'.'+fileExt)

str1 = read_pdf_PDFMINER(fullFile)

knownProtocolList = [
    '36 31 30 31 31 30 30 31',
    '36 31 30 31 35 31 30 35'
]

pathName = ''
fileName = 'log'

knownProtocolList = None

protocolList = FindUnknownProtocolList(pathName, knownProtocolList = knownProtocolList,
                        inputFileName=fileName, savePathName='', 
                        saveFileName='log_result2', fileExt='txt')

print(protocolList)

protocolLines = protocolList.split('\n')
print(protocolLines)


str2 = " ".join(str1.splitlines())
str3 = str2.replace("   ", " ")

for line in protocolLines:

    idx = str3.find(line[0:26])

    if idx != -1:   
        str4 = str3[idx:idx+2000]
        idx2 = str4.find('0060.282-31')
        print("Look at the Page :" + str4[idx2+11:idx2+17])

# save_string_to_text(str1, savePathName=pathName, saveFileName='sample_result1')
# save_string_to_text(str2, savePathName=pathName, saveFileName='sample_result2')
# save_string_to_text(str3, savePathName=pathName, saveFileName='sample_result3')
# save_string_to_text(str4, savePathName=pathName, saveFileName='sample_result4')