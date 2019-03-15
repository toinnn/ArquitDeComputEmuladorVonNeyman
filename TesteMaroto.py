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
print(n)
"""
def chama (x,y) :
    print("OLA")
    print(x+y)
dicionario={"mov":lambda x,y :chama(x,y)}
dicionario["mov"](1,2)
print(bytearray("mov"))
"""