import re
from typing import List

from IPython import embed
def HexToDec ():
    print("Eu vou transformar hexa em decimal")
class Registrador :
    def __init__(self):
        print("Ainda nao faço nada")
class CPU :
    def __init__(self):
        print("Ainda nao faço nada")
    A=B=C=D=Pi=Registrador

class RAM :
    def __init__(self):
        print("Ainda nao faço nada")
class Barramento :
    def __init__(self):
        print("Ainda nao faço nada")
        self.CPU =[None]*43
        self.ES=[None]*43
        self.RAM=[None]*43

    def leituraES (self,dado) :
        print("nao faço nada")
        for n in range(len(self.ES))
            if self.ES[n]==None and len(dado) :
                self.ES[n]=dado[0]
                dado.popleft()


class ES :
    def __init__(self):
        self.buffer[64]
        for n in range(0,64,1):
            self.buffer[n] =None

    def escrita (self,Barramento) :
        print("Ainda nao faço nada")

    def aloca (self,num) :
        if self.buffer[63] !=None :
            self.escrita()
        for n in range(64):
            if self.buffer[n]==None :
                self.buffer[n]=num
                print("{} alocado na posição {} do Buffer de E\\S".format(num,n))

    def Encoder(self,codigo) :
        if codigo[1] =="mov" :
            self.aloca(1)
            self.aloca(codigo[2])
    def Parser (self,codigo):
        input_string= "mov A, 2"
        ex = r"(mov)\s+([\daAbBcCdDeEfF]*),\s+(\d+)"
        m=re.match(ex,codigo)
        if m :
