#Program to pull and sort a pdf set based on an index csv file
#By Patrick Young, 5-21-21

import PyPDF2, csv, pandas as pd

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

#Open CSV file with pdf indexing locations, get length of csv file
def openSpreadSheet(pathSS):
    with open(pathSS, newline='') as csvfile:
        EstimateIndex = csv.reader(csvfile, delimiter=',')
        list_of_rows = list(EstimateIndex)
        df = pd.DataFrame(list_of_rows)
        length_df = len(df)
        print(df)
    return df, length_df

#main iteration process. Look at each row one at a time
#and pull name, year, and range information. Look at corresponding pages
#in the PDF.
def sortProcess(n):
    pdf_writer =  PdfFileWriter()
    #Unsure if the below line is necessary, but without it and
    #pdfFileObj.close(), ran into memory errors
    pdfFileObj = open(pathPDF, 'rb')
    pdf = PdfFileReader(pdfFileObj)
    
    name = df.loc[n][0]
    year = df.loc[n][1]
    start = int(df.loc[n][2])
    end = int(df.loc[n][3])
    for page in range(start - 1, end):
        pdf_writer.addPage(pdf.getPage(page))
        
    output = f'{year}_{name}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    pdfFileObj.close()
       

#Lines to activate code
if __name__=='__main__':
    pathSS = 'CostEstimatesIndex.csv'
    pathPDF = 'KPFF SPD Tacoma Cost Estimate Info.pdf'
    n = 1
    df, length_df = openSpreadSheet(pathSS)
    
    while n < length_df:
        sortProcess(n)
        n += 1
