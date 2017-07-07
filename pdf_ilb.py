import os, datetime
from PyPDF2 import PdfFileMerger
#directories =["L:\\AMDT_0_CHARTS\\COCESNA\\AD\\MHLM\\original"]
#directories =["L:\\AMDT_0_CHARTS\\COCESNA\\ENR\\original"]
#directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\02_ENR\\letter"]
directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\02_ENR\\tabloid"]
merger = PdfFileMerger()

list = []

for n in directories:
    for s in os.listdir(n):
        list.append(s)
        #merger.append('%s\\%s'%("L:\\AMDT_0_CHARTS\\COCESNA\\AD\\MZBZ",s))
        #merger.append('L:\mxd_versioned\TEMPLATES\INTENTIONALLY LEFT BLANK_letter.pdf')
        #merger.write('_%s'%s)

#print list

for n in list:
    print n
    merger.append('%s\\%s'%(directories[0],n))
    #merger.append('L:\mxd_versioned\TEMPLATES\INTENTIONALLY LEFT BLANK_letter.pdf')
    merger.append('L:\mxd_versioned\TEMPLATES\INTENTIONALLY LEFT BLANK_tabloid_landscape.pdf')
    merger.write('%s\\tt\\%s.pdf'%(directories[0],os.path.splitext(n)[0]))
    merger = PdfFileMerger()
    #merger.close()
    #,datetime.datetime.now().strftime("%Y%m%d")