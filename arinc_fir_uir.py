# import required python modules
import csv

with open('L:\\OTROS\\2017\\00003_ARINC424_NAVTECH\\cocesna1613\\cocesna1613.dat', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     count = 0
     # empty list to store FIR
     fir_list =[]
     for row in spamreader:
         row2=''.join(row)
#F - FIR
         #print row2[:6]
         if row2[:6] == 'SLAMUF':
             #and row2[21:22]=='1':
             count+=1
             fir_list.append(row2[6:10])

             #print row2
print '%i records'%(count)+'\n'
print 'Number of Procedures: %i'%len(sorted(list(set(fir_list))))

gid_c = 1
for s in sorted(list(set(fir_list))):
    print '%i,%s'%(gid_c,s)
    gid_c+=1


