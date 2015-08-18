#!/usr/bin/python

import re,sys

file=open(sys.argv[1],"r")
temp=float(sys.argv[2])
molnum=float(sys.argv[3])

fileline=file.readlines()
#dh=open("pot_ave.dat", "w")
z=[]
e=[]
n=[]
def grep(string,file,n,z,t,num):
    expr = re.compile(string)
    for text in fileline:
        match = expr.search(text)
        if match != None:
            x=match.string
            y=list(x.split())
            z.append(float(y[n]))
            if n==13:
                energy=sum(z)*4.186/(len(z)*num)
 #               dh.write('%s \n' % energy) 
    return z

grep("ENERGY:  ",file,13,e,temp,molnum)
energy=sum(e)*4.186/(len(e)*molnum)

print 'INTERNAL ENERGY: ' + str(energy) + ' kJ/mol\n'
