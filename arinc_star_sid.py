import csv
#airport_list = ['MZBZ','MGGT','MGMM','MHTG','MHLM','MHRO','MHLC','MSLP','MSSS','MNMG','MROC','MRLB','MRPV','MRLM']
airport_list = ['MSLP']
#with open('C:\\erase\\FAA\\cifp_201704\\FAACIFP18.dat', 'rb') as csvfile:
#with open('C:\\erase\\MSLP_MGGT.dat', 'rb') as csvfile:

with open('L:\\OTROS\\2017\\00003_ARINC424_NAVTECH\\cocesna1613\\cocesna1613.dat', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     count = 0
     sid_list =[]
     for row in spamreader:
         row2=''.join(row)
         for a in airport_list:
#D - DEPARTURE
#E - ARRIVAL
            # if row2[:5] == 'SLAMP' and row2[6:10]== a and row2[12:13]=='E' and row2[13:19]=='OLAAA1':
             if row2[38:39]=='1' and row2[:13] == 'SLAMP %s%sD'%(a,a[:2]) :
                 #and row2[21:22]=='1':
                 count+=1
                 sid_list.append(row2[13:19])

                 print row2
print '%i records'%(count)+'\n'
print 'Number of Procedures: %i'%len(sorted(list(set(sid_list))))

gid_c = 1
for s in sorted(list(set(sid_list))):
    print '%i,%s'%(gid_c,s)
    gid_c+=1


