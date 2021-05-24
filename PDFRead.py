#Program to pull and sort a pdf set based on an index csv file
#By Patrick Young, 5-21-21

import PyPDF2, csv, pandas as pd

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

#main iteration process. Look at each row one at a time
#and pull name, year, and range information. Look at corresponding pages
#in the PDF.
def sortProcess(n):
    name = df.loc[n][0]
    year = df.loc[n][1]
    start = int(df.loc[n][2])
    end = int(df.loc[n][3])
    
    pdf_writer =  PdfFileWriter()
    #Unsure if the below line is necessary, but without it and
    #pdfFileObj.close(), ran into memory errors
    # The with open(... is one way to automatically make sure that the 
    # file objects actually get closed
    with open(pathPDF, 'rb') as pdfFileObj:
        pdf = PdfFileReader(pdfFileObj)

        for page in range(start - 1, end):
            pdf_writer.addPage(pdf.getPage(page))

        with open(f'{year}_{name}.pdf', 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
           

#Lines to activate code
if __name__=='__main__':
    pathSS = 'CostEstimatesIndex.csv'
    pathPDF = 'KPFF SPD Tacoma Cost Estimate Info.pdf'
    df = pd.read_csv(pathSS)
    
    # if you want to level up this loop check out the apply function in pandas
    # will look into it! -PY
    for n in range(len(df)):
        sortProcess(n)
