import re
from typing import List

from IPython import embed
def HexToDec ():
    print("Eu vou transformar hexa em decimal")
class Registrador :
    def __init__(self):
        print("Ainda nao faço nada")
        self.Memoria=bytes
class CPU :
    def __init__(self,Barramento):
        print("Ainda nao faço nada")
        self.Barramento=Barramento
        self.Decoder={"mov".encode("utf-8"):lambda E,i:self.mov(E,i),"add".encode("utf-8"):lambda x,y :self.add(x,y),"inc".encode("utf-8"):lambda x:self.inc(x),"imul".encode("utf-8"):lambda x,y,z : self.imul(x,y,z)}
    A=B=C=D=Pi=Registrador
    def leituraRAM(self):
        self.Barramento.SolicitaçãoRamDaCPU()
    def exec (self) :
        print("nao faço nada")
    def mov (self,E,i) :
        print("nao faço nada")
    def add(self,x,y):
        print("nao faço nada")
    def inc(self,x):
        print("nao faço nada")
    def imul(self,x,y,z):
        print("não faço nada")

class RAM :
    def __init__(self,Barramento):#Falta validar o tamnho dos dados que circulam na RAM
        print("Ainda nao faço nada")
        self.Barramento=Barramento
        self.Memoria=bytearray(128)
        self.MemoriaAlocada=0
    def leituraBarramento(self):
        self.Memoria[self.MemoriaAlocada:self.MemoriaAlocada+len(self.Barramento.escritaRam())]=self.Barramento.escritaRam()
        self.MemoriaAlocada+=len(self.Barramento.escritaRam())
    def escritaBarramento(self):
        if self.MemoriaAlocada >=32 :
            self.Barramento.leituraRAM(self.Memoria[0:33])
            self.MemoriaAlocada-=32
        else :
            self.Barramento.leituraRAM(self.Memoria[0:33])
            self.MemoriaAlocada -=len(self.MemoriaAlocada)


class Barramento :
    def __init__(self):
        print("Ainda nao faço nada")
        self.CPU =bytearray(32)
        self.ES=bytearray(32)
        self.RAM=bytearray(32)
        self.ESpreenchido=0
        self.CPUpreenchido = 0
        self.RAMpreenchido = 0
        self.CPUfísica
        self.RAMfísica
        self.ESfísica
        self.auxClockRam=0
    def link (self,CPU,RAM,ES ):
        self.CPUfísica=CPU
        self.RAMfísica=RAM
        self.ESfísica=ES
    def leituraES (self,dado) :
        print("nao faço nada")
        for n in range(self.ESpreenchido,self.ESpreenchido+len(dado)) :
            self.RAM[n]=dado[0]
            dado.pop(0)
            self.ESpreenchido+=1
    def leituraRAM (self) :
        print("Ola mundo")
    def SolicitaçãoRamDaCPU(self) :
        print("oi eu sou o mundo")
        self.RAMfísica.

    def escritaRam (self) :
        if self.RAMpreenchido>=32 :
            self.RAMpreenchido-=32
            return  self.RAM[0:33]
        else:
            self.RAMpreenchido-=self.RAMpreenchido
            return self.RAM[0:self.RAMpreenchido]

class ES :
    def __init__(self,barramento):
        self.buffer=bytearray(64)
        self.preenchido=0
        self.Barramento=barramento

    def escrita (self,Barramento) :
        print("Ainda nao faço nada")
        if self.preenchido>32 :
            self.preenchido-=32
            self.Barramento.leituraES(self.buffer[0:33])
        else:
            self.Barramento.leituraES(self.buffer[0:len(self.preenchido())])
            self.preenchido = 0


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
            comando=bytearray([1])
            comando.extend(int(codigo[2]),int(codigo[3]))
            self.aloca(comando)
        elif codigo[1]=="add" :
            comando = bytearray([2])
            comando.extend()

    def Parser (self,codigo):
        input_string= "mov A, 2"
        ex = r"(mov)\s+0x([\d]*),\s+(\d+)"
        m=re.match(ex,codigo)
        add=re.match(r"(add)\s+0x(\d+),\s+|",codigo)
        if m :
            self.Encoder(codigo)
