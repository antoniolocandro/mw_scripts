# import required python modules
import csv
#airport_list = ['MZBZ','MGGT','MGMM','MHTG','MHLM','MHRO','MHLC','MSLP','MSSS','MNMG','MROC','MRLB','MRPV','MRLM']
airport_list = ['FAOR']
with open('L:\\OTROS\\2017\\00003_ARINC424_NAVTECH\\cocesna1613\\cocesna1613.dat', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     count = 0
     sid_list =[]
     for row in spamreader:
         row2=''.join(row)
         for a in airport_list:
#F - APPROACH
            if (row2[:13] == 'SLAMP %s%sF'%(a,a[:2]) and row2[19:20]=='A' and row2[26:28]=='010') :
            #if (row2[:13] == 'SAFRP %s%sF'%(a,a[:2])):
                 #and row2[21:22]=='1':
                 count+=1
                 sid_list.append('%s,%s'%(a,row2[13:18]))
                 #print row2[26:28]
                 print row2
print '%i records'%(count)+'\n'
print 'Number of Procedures: %i'%len(sorted(list(set(sid_list))))

gid_c = 1
for s in sorted(list(set(sid_list))):
    print '%i,%s'%(gid_c,s)
    gid_c+=1


