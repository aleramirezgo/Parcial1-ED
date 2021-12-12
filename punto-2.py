import math

class Node():
    def __init__(self, dato):
        self.data=dato
        self.next=None

    def setDistancia(self, forX, forY, a, l):
        tempx=0
        tempy=self.data.y-forY*l
        if(l%2==0):
            tempx=self.data.x-forX*a
        else:
            tempx=self.data.x-forX*(a+1)
        self.data.distancia=tempx+a*(tempy-1)
        #print(self.data.distancia)

    def printer(self):
         print("[",self.data.id,",",self.data.x,",",self.data.y,"]")

    def getId(self):
        return self.data.id

    def getX(self):
        return self.data.x

    def getY(self):
        return self.data.y

    def getDistancia(self):
        return self.data.x

    

class SingleLinkedList():
    def __init__(self):
        self.head=None

    def addEnd(self, data):
        nuevo = Node(data)
        if self.head == None:
            self.head = nuevo
        else:
            temporal=self.head
            while temporal.next != None:
                temporal=temporal.next
            temporal.next = nuevo

    def printer(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" "),
            temp = temp.next

    def packprinter(self,n):
        temp = self.head
        while n>0:
            pack1=temp.data
            pack1.printer()
            temp = temp.next
            n-=1

    def intSplitRemake(self, str):
        str=str+" "
        y=0
        for x in str:
            if x == " ":
                self.addEnd(y)
                y=0
            else:
               y=y*10+int(x)

    def packager(self,n):
        temp1=self.head
        temp2=SingleLinkedList()
        while n>0:
            id=temp1.data
            temp1 = temp1.next
            x=temp1.data
            temp1 = temp1.next
            y=temp1.data
            pack=Node(Paquete(id,x,y))
            temp2.addEnd(pack)
            temp1 = temp1.next
            n-=1
        return temp2

    def pickPacket(self, x,y,a,l):
        pickedList=SingleLinkedList()
        temp=self.head
        while temp:
            checkX=temp.data.getX()
            checkY=temp.data.getY()
            if(x*a <= checkX < (x+1)*a and y*l <= checkY < (y+1)*l):
                pickedList.addEnd(temp.data)
                temp=temp.next
            else:
                temp=temp.next
        return pickedList

    def sortDistancia(self, x,y,a,l):
        current=self.head
        index = None 
        if(self.head == None):
            return
        else:
            while(current!=None):
                index = current.next #El index ahora apunta al siguiente de current

                while(index!= None):
                    index.data.setDistancia(x,y,a,l)
                    current.data.setDistancia(x,y,a,l)
                    indexDist=index.data.getDistancia()
                    currentDist=current.data.getDistancia()
                    if (currentDist > indexDist): #Si la data del nodo actual es menor que la del index, intercambiaran posicion
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index=index.next
                current = current.next

    def sort(self):
        current=self.head
        index = None

        if(self.head == None):
            return
        else:
            while(current!=None):
                index = current.next #El index ahora apunta al siguiente de current

                while(index!= None):
                    if (current.data > index.data): #Si la data del nodo actual es mayor que la del index, intercambiaran posicion
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index=index.next
                current = current.next

    def idPrinter(self):
        temp = self.head
        idString=""
        while (temp):
            idLocal=temp.data.getId()
            idString= idString+ str(idLocal)+ " "
            temp = temp.next
        return idString

    def conteo(self):
        temp=self.head
        x=0
        while temp:
            x+=1
            temp=temp.next
        return x

class Paquete():
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.distancia=0



        
if __name__ == '__main__':
    #Se asume que el gira cada 1 unidad en y hacia abajo
    #colecta de datos iniciales, ancho, largo, cantidad de regiones/camiones
    #a, l, c = map(int, input().split())  # a = Ancho de la ciudad, l = largo de la ciudad, c = numero de regiones
    #p, m = map(int, input().split()) # p = cantidad de paquetes, m = numero de montones
    lis1 = SingleLinkedList()
    line1 = input()
    lis1.intSplitRemake(line1)
    a = lis1.head.data
    l = lis1.head.next.data
    c = lis1.head.next.next.data

    #colecta de numero de paquetes y numero de montones
    lis2 = SingleLinkedList()
    line1 = input()
    lis2.intSplitRemake(line1)
    p = lis2.head.data
    m = lis2.head.next.data

    #colecta de todos los datos de los paquetes en cada monton y agrupacion en paquetes
    lis3 = SingleLinkedList()
    for x in range(0,m):
        line1=input()
        lis3.intSplitRemake(line1)
    #lis3.printer()
    #print()
    lis4 = lis3.packager(p)
    #lis4.packprinter(p)


    # numero de regiones a lo largo y ancho es el mismo, ahora se calcula las dimensiones de cada region
    rootC = int(math.sqrt(c))
    aRegion = a/rootC
    lRegion = l/rootC

    #no hace falta tener c listas enlazadas activas a la vez solo hace falta ejecutar la misma funcion c numero de veces
    n = 0
    for y in range(0,rootC):
        for x in range(0,rootC):
            camion = SingleLinkedList()
            n += 1 #n = n+1
            camion = lis4.pickPacket(x, y, aRegion, lRegion)
            countcamion=camion.conteo()
            #print(countcamion)
            #camion.printer()
            #camion.packprinter(countcamion)
            camion.sortDistancia(x,y, aRegion, lRegion)
            huellas=camion.idPrinter()
            print(str(n)," ",huellas)


    



#crear c camiones(pilas)/ CREAR SOLO 1 CAMION, VACIARLO CADA VEZ  
#leer lis4 y asignar los paquetes a su respectivo camion
#calcular la sitancia de envio esgun el orde zig-zag
# organizar los paquetes con el calculo de distancia
# imprimir 
