import os
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def read_pdf_PDFMINER(pdf_file_path):
    """
    pdf_file_path: 'dir/aaa.pdf'로 구성된 path로부터 
    내부의 text 파일을 모두 읽어서 스트링을 리턴함.
    https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
    """
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


pathName = ''
fileName = 'sample'
fileExt = 'pdf'
fullFile = os.path.join(pathName, fileName+'.'+fileExt)

str1 = read_pdf_PDFMINER(fullFile)
str2 = " ".join(str.splitlines())

save_string_to_text(str1, savePathName=pathName, saveFileName='sample_result1')
save_string_to_text(str2, savePathName=pathName, saveFileName='sample_result2')