d1 = {1:2,3:4,5:6}
print d1.keys()
print d1.values()
print ""

print d1[1]
print d1[3]
print ""

d1[1] = 3
print d1

for key in d1.keys():
    print (key,d1[key])

print ""

for key,value in d1.items():
    print (key,value)
print ""

d2 = {'abc':'ac','love':['lian','shenheng','1','2'],2:3}
#print d2
#print d2.items()

print d2.get(2)
print d2.__class__
d3 = d2.copy()
d2[2] = 5
print d2
print d3


for key,value in d2.items():
    print str(key) + ':' + str(value)
