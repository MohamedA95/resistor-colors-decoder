colures={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'gray':8,'white':9,'gold':0.1,'silver':0.01}
tolerance={'gold':5,'silver':10,'brown':1,'red':2,'green':0.5,'blue':0.25,'violet':0.1,'grey':0.05}

while 1:
  x=raw_input("enter the colors names sprated by spaces \n enter -1 to stop the program \n")
  if x =='-1':
    print 'see you latter :)'
    break  
  x=x.lower()
  x=x.split()
  
  if x[0] not in colures :
    print "unknown color ",x[0],"\n allowed colors are \n",colures.keys(),"\n"
    continue
  if x[1] not in colures :
    print "unknown color ",x[1],"\n allowed colors are \n",colures.keys(),"\n"
    continue
  if x[2] not in colures :
    print "unknown color ",x[2],"\n allowed colors are \n",colures.keys(),"\n"
    continue
  if x[3] not in tolerance:
    print "unknown color ",x[3],"\n allowed colors are \n",tolerance.keys(),"\n"
    continue 
  print colures[x[0]]*10+colures[x[1]],'x10^',colures[x[2]],'with tolerance of ± ',tolerance[x[3]],'%'
