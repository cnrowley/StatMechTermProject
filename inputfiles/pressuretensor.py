import os, sys

fh=open(sys.argv[1], 'r')
lines=fh.readlines()

pxx=[]
pyy=[]
pzz=[]

for l in lines:
    if(l[0:9]=='PRESSURE:'):
        f=l.split()
        pxx.append(float(f[2]))
        pyy.append(float(f[6]))
        pzz.append(float(f[10]))

pxx_sum=0.0
pyy_sum=0.0
pzz_sum=0.0

for p in pxx[len(pxx)/2:]:
    pxx_sum=pxx_sum+p

for p in pyy[len(pxx)/2:]:
    pyy_sum=pyy_sum+p

for p in pzz[len(pxx)/2:]:
    pzz_sum=pzz_sum+p

print 'Pxx = ' + str(pxx_sum/(len(pxx)/2)) + ' bar'
print 'Pyy = ' + str(pyy_sum/(len(pyy)/2)) + ' bar'
print 'Pzz = ' + str(pzz_sum/(len(pzz)/2)) + ' bar'

gamma=0.5*
