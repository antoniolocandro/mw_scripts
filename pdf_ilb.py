import os, datetime
from PyPDF2 import PdfFileMerger, PdfFileReader
#directories =["L:\\AMDT_0_CHARTS\\COCESNA\\AD\\MHLM\\original"]
#directories =["L:\\AMDT_0_CHARTS\\COCESNA\\ENR\\original"]
#directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\02_ENR\\letter"]
#directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\02_ENR\\tabloid"]
#directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\02_ENR\\"]
#directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\03a_AD_index\\"]
directories =["L:\\AMDT_0_CHARTS\\HONDURAS\\03b_AD\\MHTG\\"]
merger = PdfFileMerger()

list = []

# get file source
for n in directories:
    for s in os.listdir(n):
        list.append(s)
        # debug operation
        #print s
        # Get PDF size
        #in2 = PdfFileReader('%s\\%s' % (directories[0], s)).getPage(0).mediaBox
        #if in2[2] == 612:
         #   size = "letter_portrait"
        #elif in2[2] == 1224:
         #   size = "tabloid_landscape"
        #else:
         #   size = "letter_portrait"
        # print in2[2]
        #print s,'\n',size,'\n'

#print list

for n in list[0:len(list)-1]:
    print n

    in3 = PdfFileReader('%s\\%s'%(directories[0],n)).getPage(0).mediaBox
    #print in3
    if in3[2] == 612:
        size = "letter_portrait"
        print size
        merger.append('%s\\%s'%(directories[0],n))
        merger.append('L:\mxd_versioned\TEMPLATES\INTENTIONALLY LEFT BLANK_letter.pdf')
        merger.write('%s\\tt\\%s.pdf'%(directories[0],os.path.splitext(n)[0]))
        merger = PdfFileMerger()
        # merger.close()
        # ,datetime.datetime.now().strftime("%Y%m%d")
    elif in3[2] == 1224:
        size = "tabloid_landscape"
        print size
        merger.append('%s\\%s'%(directories[0],n))
        #print '%s\\%s'%(directories[0],n)
        merger.append('L:\mxd_versioned\TEMPLATES\INTENTIONALLY LEFT BLANK_tabloid_landscape.pdf')
        merger.write('%s\\tt\\%s.pdf'%(directories[0],os.path.splitext(n)[0]))
        merger = PdfFileMerger()
        # merger.close()
        # ,datetime.datetime.now().strftime("%Y%m%d")
    else:
        pass

print "-------------------- finished --------------------"