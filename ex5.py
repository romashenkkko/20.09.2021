
x=[34,6,43,12,32]
y=x
print('suma primelor trei componente ale variabilei x este', sum(x[0:3]))
print('suma tuturor componentelor variabilei y este', sum(y))
p=1
for i in range(0, len(x)):
    p=p*x[i]
    i+=1
print('produsul tuturor componentelor variabilei x este ', p)
print('valoarea absolută a componentei a treia a variabilei y este ', abs(x[2]))
print('suma primelor componente ale variabilelor x şi y este', x[0]+y[0]