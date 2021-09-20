
t=[12,3,23,14,25,16,6,7,4,11,2,8,9,10,17,30,28,15,18,19,-3,-6,-1,0]
print('1. temperatura medie este', sum(t)/24)
print('2. maximul temperaturii este ', max(t), 'iar minimul este', min(t))
for i in t:
    if i==max(t):
        print('ora la care s-a înregistrat temperatura maximă este', t.index(1)+1) 
for i in t:
    if i==min(t):
        print('3. ora la care s-a înregistrat temperatura minimă este', t.index(1)+1)
n1=0
for i in t:
    if i<0:
        n1+=1
print('4. numărul de zile în care au fost înregistrate temperaturi mai jos de zero grade este', n1)
n2=0
for i in t:
    if i>sum(t)/24:
        n2+=1
print('5. numărul de zile în care au fost înregistrate temperaturi mai mari de media săptămânală este ', n2)