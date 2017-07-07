import csv
import subprocess
import os

ip_list=[]


#ip_list=["172.16.39.120","172.16.38.111","172.16.38.140"]

with open(os.devnull, "wb") as limbo:
        with open('C:\\Users\\Antonio\\Desktop\\ip_list.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(spamreader, None)
            count=0
            with open('C:\\Users\\Antonio\\Desktop\\estado_estaciones.csv', 'wb') as csvfile2:
                spamwriter = csv.writer(csvfile2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['%s,%s,%s,%s,%s' % ('gid', 'ip', 'nombre_estacion', "estado", 'ubicacion')])

                for row in spamreader:

                # row2 = ''.join(row)
                    ip=row[0]
                    result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],stdout=limbo, stderr=limbo).wait()
                    if result:
                               print '%i;%s;%s;%s;%s'%(count,ip,row[1],"inactive",row[2])
                               spamwriter.writerow(['%i,%s,%s,%s,%s'%(count,ip,row[1],"inactive",row[2])])
                    else:
                               print '%i;%s;%s;%s;%s'%(count,ip,row[1], "active",row[2])
                               spamwriter.writerow(['%i,%s,%s,%s,%s'%(count,ip,row[1], "active",row[2])])
                #csvfile2.close()
                    count+=1


import csv
import xlsxwriter

            # if we read f.csv we will write f.xlsx
wb = xlsxwriter.Workbook('C:\\Users\\Antonio\\Desktop\\estado_estaciones.csv'.replace(".csv", ".xlsx"))
ws = wb.add_worksheet("STATION_LIST")  # your worksheet title here

with open('C:\\Users\\Antonio\\Desktop\\estado_estaciones.csv', 'r') as csvfile:
    table = csv.reader(csvfile)
    i = 0
                # write each row from the csv file as text into the excel file
                # this may be adjusted to use 'excel types' explicitly (see xlsxwriter doc)
    for row in table:
        ws.write_row(i, 0, row)
        i += 1
ws.autofilter('A1:E2000')
ws.filter_column('D', 'x == inactive')

format1 = wb.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
ws.conditional_format('D2:D2000', {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'inactive',
                                       'format':   format1})
wb.close()