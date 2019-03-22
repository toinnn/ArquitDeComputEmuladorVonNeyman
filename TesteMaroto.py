import re
import bitstream
from IPython import embed
"""
input_string= "mov A, 2"
ex=r"(mov)\s+([\daAbBcCdDeEfF]*),\s+(\d+)"
expression = r"mov\s+\w+,\s+\d+"
m=re.match(ex,"mov A23eF, 23")
print(m[2])
"""
ex =r"(mov)\s+0x([\d]*),\s+(\d+)"
m=re.match(ex,"mov 0x03, 30")
m[1].encode('utf-8')
li=[m[1].encode('utf-8')]
n=bytearray([2])
n.extend([int(m[2]),int(m[3])])
n.append(250)
#j=int.from_bytes(n[2],byteorder='big',signed=true)
j=int(n[3])
print(n)
print(n[1])
print(n[2])
n[3]=n[2]+n[1]
print(n[3])

k=321
cunc=str(n[2])+str(n[1])
print(cunc[0:3])
k=int(cunc[0:3])
print(k+n[2])

lista=[]
lista.append("oi")
print(lista[0])
"""
separator = ' '
array = [r'_', r'_', r'_', r'_', r'_', r'_', r'_']
result = [separator.join(n[1:3])]
print(result)"""

"""
juao=[2,3,5,4,8,6,2,9]
aux=juao[2:5]
del juao[2:5]
juao.extend([2])
print(aux)
print(juao)
"""
"""
def chama (x,y) :
    print("OLA")
    print(x+y)
dicionario={"mov":lambda x,y :chama(x,y)}
dicionario["mov"](1,2)
#print(bytearray("mov"))
"""