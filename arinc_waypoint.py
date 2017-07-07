# import required python modules
import csv

#route_lookup="J93"

#with open('C:\\erase\\FAA\\cifp_201704\\FAACIFP18.dat', 'rb') as csvfile:
with open('L:\\OTROS\\2017\\00003_ARINC424_NAVTECH\\cocesna1613\\cocesna1613.dat', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     count = 0
     # empty list to store ENR
     enr_list =[]
     for row in spamreader:
         row2=''.join(row)
#EA - EN ROUTE WAYPOINTS
#ER - EN ROUTE AIRWAYS
         #print row2[:6]
         #if row2[13:18]== 'J93  ':
         #if row2[:5] == 'SUSAP' and row2[12:13]=='C' :
         #if row2[:6] == 'SLAMER':
         #if row2[:5] == 'SLAMP' and row2[34:36]=='MM' :
         #if row2[38:39]=='1' and row2[13:18]== 'J93  ':
         #if (row2[:6] == 'SLAMER' or row2[:6] == 'SUSAER' or row2[:6] == 'SSAMER') and row2[34:36]=='MM' and row2[38:39] == '1' and row2[13:18] == 'J93  ':
             count+=1
             enr_list.append(row2[13:18])

             print row2[:6],row2[25:29],row2[13:18],row2[29:34],row2[83:88],row2[93:98],row2[32:51]
print '%i records'%(count)+'\n'
print 'Number of Procedures: %i'%len(sorted(list(set(enr_list))))

gid_c = 1
#for s in sorted(list(set(enr_list))):
 #   print '%i,%s'%(gid_c,s)
  #  gid_c+=1