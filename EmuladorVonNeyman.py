import re
from typing import List

from IPython import embed
def HexToDec ():
    print("Eu vou transformar hexa em decimal")

class Registrador :
    def __init__(self):
        #print("Ainda nao faço nada")
        self.Memoria=bytearray(4)
        self.Stock=0
    def recebe(self,valor) :#Ele recebe um byte array
        if len(valor)==4 :
            self.Memoria=valor
        else:
            self.Memoria=bytearray(4-len(valor))
            self.Memoria.extend(valor[0:len(valor)])
    def dado (self):
        return self.Memoria
    def valor(self):
        return int(str(self.Memoria[0]) + str(self.Memoria[1]) +str(self.Memoria[2]) +str(self.Memoria[3]))

class CPU :
    def __init__(self,Barramento):
        #print("Ainda nao faço nada")
        self.Barramento=Barramento#Prescisa rearrumar o Decoder :
        self.Decoder={1:lambda argumento:self.mov(argumento),2:lambda argumento :self.add(argumento) , 3:lambda argumento:self.addNum(argumento) , 4:lambda x:self.inc(x),5:lambda argumento : self.imul(argumento),6 :"futuro"}
        self.PiDict={1:lambda :self.A ,2:lambda :self.B ,3:lambda :self.C,4:lambda :self.D,5:lambda :self.Pi}
        self.A=Registrador()
        self.B =Registrador()
        self.C =Registrador()
        self.D =Registrador()
        self.Pi =Registrador()
        self.Pi.recebe(bytearray([1]))

    """def leituraRAM(self):
    self.Barramento.SolicitaçãoRamDaCPU()"""
    def leituraBarramento(self):#Implementar a execução dentro da leitura
        aux=self.Barramento.escritaCPU()
        auxPi=1
        while self.PiDict[self.Pi.valor()].valor()!=0 :
            self.IncremPi()
        self.PiDict[self.Pi.valor()].recebe(aux)



    def IncremPi(self):
        if self.Pi.valor()<5 :
            self.Pi.recebe(1+self.Pi.valor())
        else:
            self.Pi.recebe(1)
    #ImcremPi() Move o local ao qual o registrador Pi aponta

    def show(self):
        print("Registrador A : "+self.A.valor())
        print("Registrador B : " + self.B.valor())
        print("Registrador C : " + self.C.valor())
        print("Registrador D : " + self.D.valor())
        print("Registrador Pi : " + self.Pi.valor())

    def exec (self) :
        aux=self.PiDict[self.Pi.valor()].valor()
        argumTaman=0
        if aux==1 :
            argumTaman=3
        elif aux==2 :
            argumTaman=3
        elif aux==3 :
            argumTaman=3
        elif aux==4 :
            argumTaman=2
        elif aux ==5 :
            argumTaman=4
        elif aux ==6 :
            argumTaman=4
        ListArgument=[]
        self.IncremPi()
        while self.PiDict[self.Pi.valor()].valor != 0 :#Se o reset ao fim de execução de código for remmovido aki vai ter que ser mechido
            ListArgument.append(self.PiDict[self.Pi.valor()].valor)
            self.IncremPi()

        if len(ListArgument)==argumTaman-1 :
            self.Decoder[aux](ListArgument)
            self.show()
            self.A.recebe(0)
            self.B.recebe(0)
            self.C.recebe(0)
            self.D.recebe(0)
            self.Pi.recebe(1)
        else:
            self.show()
            self.Pi.recebe(1)
            return


        """aux=self.PiDict[self.Pi.valor()].valor()
        self.PiDict[self.Pi.valor()].recebe(0)
        self.IncremPi()
        #Montar a lista com os parametros da função...
        self.Decoder[self.PiDict[self.Pi.valor()].valor()]()
        """
        #print("nao faço nada")
    def mov (self,argumento) :
        R=argumento[0]
        i=argumento[1]
        self.PiDict[R].recebe(bytearray([i]))
        print("Agora eu faço + falta coisa ainda")
    def add(self,argumento):#Acho que esse add ta pronto
        x=argumento[0]
        y=argumento[1]

        R1Dado=self.PiDict[x].dado()
        R2Dado=self.PiDict[y].dado()

        aux1=str(R1Dado[0])+str(R1Dado[1])+str(R1Dado[2])+str(R1Dado[3])
        aux2 = str(R2Dado[0]) + str(R2Dado[1]) + str(R2Dado[2]) + str(R2Dado[3])
        resultado= int(aux1)+int(aux2)
        aux1=str(resultado)
        resultadoByte=bytearray(4)
        n=0
        while len(aux1)!=0 and n <4 :

            if len(aux1)>=4 :
                resultado = int(aux1[len(aux1) - 4:len(aux1)])
            else:
                resultado = int(aux1[0:len(aux1)])
            if resultado > 255:
                aux2=str(resultado)
                aux2=aux2[1:3:]
                aux1=aux1[0:len(aux1)-2:]
                resultadoByte[n]=int(aux2)
            else:
                resultadoByte[n]=resultado
                aux1=aux1[0:len(aux1)-3:]
            n += 1
        self.PiDict[x].recebe(resultadoByte)


        print("nao faço nada")
    def addNum(self,argumento):
        x = argumento[0]
        y = argumento[1]

        R1Dado = self.PiDict[x].dado()

        aux1 = str(R1Dado[0]) + str(R1Dado[1]) + str(R1Dado[2]) + str(R1Dado[3])
        resultado=int(aux1)+y
        aux1 = str(resultado)
        resultadoByte = bytearray(4)
        n = 0
        while len(aux1) != 0 and n < 4:

            if len(aux1) >= 4:
                resultado = int(aux1[len(aux1) - 4:len(aux1)])
            else:
                resultado = int(aux1[0:len(aux1)])
            if resultado > 255:
                aux2 = str(resultado)
                aux2 = aux2[1:3:]
                aux1 = aux1[0:len(aux1) - 2:]
                resultadoByte[n] = int(aux2)
            else:
                resultadoByte[n] = resultado
                aux1 = aux1[0:len(aux1) - 3:]
            n += 1
        self.PiDict[x].recebe(resultadoByte)
    def inc(self,argumento):
        x=argumento[0]
        self.addNum(x,1)
        print("eu uso o add")
    def imul(self,argumento):
        x=argumento[0]
        y=argumento[1]
        z=argumento[2]

        R1Dado=self.PiDict[x].dado()
        R2Dado=self.PiDict[y].dado()
        R3Dado=self.PiDict[z].dado()

        aux1=str(R1Dado[0])+str(R1Dado[1])+str(R1Dado[2])+str(R1Dado[3])
        aux2=str(R2Dado[0])+str(R2Dado[1])+str(R2Dado[2])+str(R2Dado[3])
        aux3=str(R3Dado[0])+str(R3Dado[1])+str(R3Dado[2])+str(R3Dado[3])

        resultado=int(aux1)*int(aux2)*int(aux3)

        aux1 = str(resultado)
        resultadoByte = bytearray(4)
        n = 0
        while len(aux1) != 0 and n < 4:

            if len(aux1) >= 4:
                resultado = int(aux1[len(aux1) - 4:len(aux1)])
            else:
                resultado = int(aux1[0:len(aux1)])
            if resultado > 255:
                aux2 = str(resultado)
                aux2 = aux2[1:3:]
                aux1 = aux1[0:len(aux1) - 2:]
                resultadoByte[n] = int(aux2)
            else:
                resultadoByte[n] = resultado
                aux1 = aux1[0:len(aux1) - 3:]
            n += 1
        self.PiDict[x].recebe(resultadoByte)

        #print("não faço nada")

class RAM :
    def __init__(self,Barramento):#Falta validar o tamnho dos dados que circulam na RAM
        #print("Ainda nao faço nada")
        self.Barramento=Barramento
        self.Memoria=bytearray(128)
        self.MemoriaAlocada=0
    def leituraBarramento(self):
        self.Memoria[self.MemoriaAlocada : self.MemoriaAlocada+len(self.Barramento.escritaRam())]=self.Barramento.escritaRam()
        self.MemoriaAlocada+=len(self.Barramento.escritaRam())
    def escritaBarramento(self):
        if self.MemoriaAlocada >=4 :
            self.Barramento.leituraRAM(self.Memoria[0:4])
            self.MemoriaAlocada-=4
        else :
            self.Barramento.leituraRAM(self.Memoria[0:self.MemoriaAlocada])
            self.MemoriaAlocada =0


class Barramento :
    def __init__(self):
        #print("Ainda nao faço nada")
        self.CPU =bytearray(4)
        self.ES=bytearray(4)
        self.RAM=bytearray(4)
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
    def leituraES (self,dado,RAMpreenchido) :
        #print("nao faço nada")
        for n in range(self.RAMpreenchido,self.RAMpreenchido+len(dado)) :
            self.RAM[n]=dado[0]
            dado.pop(0)
            self.RAMpreenchido+=1
    def leituraRAM (self,dado) :
        #print("Ola mundo")
        for n in range(self.CPUpreenchido,self.CPUpreenchido+len(dado)) :
            self.CPU[n]=dado[0]
            dado.pop(0)
            self.CPUpreenchido+=1
    def SolicitaçãoRamDaCPU(self) :
        print("oi eu sou o mundo")
        #self.RAMfísica.

    def escritaRam (self) :
        if self.RAMpreenchido>=4 :
            aux = self.RAM[0:4]
            del self.RAM[0:4]
            self.RAMpreenchido-=4
            return  aux
        else:
            aux=self.RAM[0:self.RAMpreenchido]
            del self.RAM[0:self.RAMpreenchido]
            self.RAMpreenchido=0
            return aux

    def escritaCPU(self):
        if self.CPUpreenchido>=4 :
            aux= self.CPU[0:5]
            del self.CPU[0:5]
            self.CPUpreenchido-=4
            return aux
        else:
            aux=self.CPU[0:self.CPUpreenchido]
            del self.CPU[0:self.CPUpreenchido]
            self.CPUpreenchido=0
            return aux

class ES :
    def __init__(self,barramento):
        self.buffer=bytearray(64)
        self.preenchido=0
        self.Barramento=barramento
        self.EntradaDado=[]
        self.ctdEntradaDado=0

    def escrita (self) :
        print("Ainda nao faço nada")
        if self.preenchido>4 :
            self.preenchido-=4
            self.Barramento.leituraES(self.buffer[0:4])
            self.buffer=self.buffer[4::]
        else:
            print("Ainda n usei o barramento")
            dado=self.buffer[0:self.preenchido]
            self.Barramento.leituraES( dado)
            self.preenchido = 0
            self.buffer=self.buffer[len(self.buffer)::]
            print("Buffer de E\\S descarregado com sucesso")
        print("Buffer de E\\S descarregado com sucesso")


    def aloca (self,num) :
        if self.preenchido ==64 :
            self.escrita()
        for n in range(self.preenchido,len(self.buffer)) :
            self.buffer[n]=num[0]
            self.preenchido+=1
            print("{} alocado na posição {} do Buffer de E\\S".format(num[0], n))
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
        elif codigo[1]=="add" and (codigo[3]=="A"or"B"or"C"or"D"or"Pi") :
            comando = bytearray([2])

            if codigo[2]== "A" :
                comando.append(1)
            elif codigo[2]== "B" :
                comando.append(2)
            elif codigo[2]== "C" :
                comando.append(3)
            elif codigo[2] == "D":
                comando.append(4)
            elif codigo[2] == "Pi":
                comando.append(5)

            if codigo[3]== "A" :
                comando.append(1)
            elif codigo[3]== "B" :
                comando.append(2)
            elif codigo[3]== "C" :
                comando.append(3)
            elif codigo[3] == "D":
                comando.append(4)
            elif codigo[3] == "Pi":
                comando.append(5)
            self.aloca(comando)

        elif codigo[1]=="add" and codigo[3].isnumeric() :
            comando = bytearray([3])

            if codigo[2]== "A" :
                comando.append(1)
            elif codigo[2]== "B" :
                comando.append(2)
            elif codigo[2]== "C" :
                comando.append(3)
            elif codigo[2] == "D":
                comando.append(4)
            elif codigo[2] == "Pi":
                comando.append(5)

            comando.append(codigo[3])
            self.aloca(comando)
        elif codigo[1]=="inc" :
            comando=bytearray([4])

            if codigo[2]== "A" :
                comando.append(1)
            elif codigo[2]== "B" :
                comando.append(2)
            elif codigo[2]== "C" :
                comando.append(3)
            elif codigo[2] == "D":
                comando.append(4)
            elif codigo[2] == "Pi":
                comando.append(5)

            self.aloca(comando)

        elif codigo[1]=="imul" :
            comando = bytearray([5])

            if codigo[2]== "A" :
                comando.append(1)
            elif codigo[2]== "B" :
                comando.append(2)
            elif codigo[2]== "C" :
                comando.append(3)
            elif codigo[2] == "D":
                comando.append(4)
            elif codigo[2] == "Pi":
                comando.append(5)

            if codigo[3]== "A" :
                comando.append(1)
            elif codigo[3]== "B" :
                comando.append(2)
            elif codigo[3]== "C" :
                comando.append(3)
            elif codigo[3] == "D":
                comando.append(4)
            elif codigo[3] == "Pi":
                comando.append(5)

            if codigo[4]== "A" :
                comando.append(1)
            elif codigo[4]== "B" :
                comando.append(2)
            elif codigo[4]== "C" :
                comando.append(3)
            elif codigo[4] == "D":
                comando.append(4)
            elif codigo[4] == "Pi":
                comando.append(5)

            self.aloca(comando)
        elif codigo[1]=="imul" and (codigo[2].isnumeric()|codigo[3].isnumeric()):
            comando=bytearray([6])

            if codigo[2]== "A" :
                comando.append(1)
            elif codigo[2]== "B" :
                comando.append(2)
            elif codigo[2]== "C" :
                comando.append(3)
            elif codigo[2] == "D":
                comando.append(4)
            elif codigo[2] == "Pi":
                comando.append(5)


    def Parser (self,codigo):
        print("Entrou no parser")
        print("codigo de entrada:"+codigo)
        input_string= "mov A, 2"
        ex = r"(mov)\s+0x([\d]*),\s+(\d+)"
        mo=re.match(ex,codigo)
        ad=re.match(r"(add)\s+([ABCD]|Pi),\s+([ABCD]|Pi|\d+)",codigo)
        #add=re.match(r"(add)\s+0x(\d+),\s+|",codigo)
        inc=re.match(r"(inc)\s+([ABCD]|Pi)",codigo)
        im=re.match(r"(imul)\s+([ABCD]|Pi),\s([ABCD]|Pi|\d+),\s([ABCD]|Pi|\d+)",codigo)

        if mo :
            print("Parser reconhece mov")
            self.Encoder(mo)
        elif ad :
            print("Parser reconhece add")
            self.Encoder(ad)
        elif inc :
            print("Parser reconhece inc")
            self.Encoder(inc)
        elif im :
            print("Parser reconhece imul")
            self.Encoder(im)
    def Imput(self,path):
        if self.ctdEntradaDado==0 :
            with open(path,"r") as f :
                self.EntradaDado= f.readlines()
        if self.ctdEntradaDado<len(self.EntradaDado) :
            self.Parser(self.EntradaDado[self.ctdEntradaDado])
            self.ctdEntradaDado+=1
        elif self.ctdEntradaDado==len(self.EntradaDado) :
            print("Não a mais codigo a ser lido")
            self.ctdEntradaDado += 1
        else:
            return


class MaqVonNeyman :

    def __init__(self):
        self.Barramento = Barramento
        self.CPU=CPU(self.Barramento)
        self.ES=ES(self.Barramento)
        self.RAM=RAM(self.Barramento)
        self.Barramento.link(self,self.CPU,self.RAM,self.ES)

    def cicloFuncionamento(self):
        for n in range(0,3):
            self.ES.Imput("Assembly.txt")
        self.ES.escrita()




meuPc=MaqVonNeyman()
meuPc.cicloFuncionamento()
