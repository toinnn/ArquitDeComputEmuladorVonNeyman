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
        self.ES=bytearray(43)
        self.RAM=bytearray(43)
        self.ESpreenchido=0
        self.CPUpreenchido = 0
        self.RAMpreenchido = 0

    def leituraES (self,dado) :
        print("nao faço nada")
        for n in range(self.ESpreenchido,self.ESpreenchido+len(dado)) :
            



    def leituraRam (self,dado) :




class ES :
    def __init__(self,barramento):
        self.buffer=bytearray(64)
        self.preenchido=0
        self.Barramento=barramento

    def escrita (self,Barramento) :
        print("Ainda nao faço nada")
        self.preenchido=0


    def aloca (self,num) :
        if self.preenchido ==64 :
            self.escrita()
        for n in range(self.preenchido,len(self.buffer)) :
            self.buffer[n]=num[0]
            self.preenchido+=1
            print("{} alocado na posição {} do Buffer de E\\S".format(num, n))
            num.pop(0)
            if n==len(num)-1 and len(num)>0 :
                self.aloca(num)
                return
            if(len(num)==0) :
                return
    def Encoder(self,codigo) :
        if codigo[1] =="mov" :
            self.aloca(bytearray(codigo))

    def Parser (self,codigo):
        input_string= "mov A, 2"
        ex = r"(mov)\s+([\daAbBcCdDeEfF]*),\s+(\d+)"
        m=re.match(ex,codigo)
        if m :
