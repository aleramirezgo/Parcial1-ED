class Node():
    def __init__(self, dato):
        self.data=dato
        self.next=None

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

    def intSplitRemake(self, str):
        str=str+" "
        y=0
        for x in str:
            if x == " " or x == None:
                self.addEnd(y)
                y=0
            else:
               y=y*10+int(x)

    def packager(self):
        x = "cabal el que lo lea"

class paquete():
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y

lis1=SingleLinkedList()
line1= input()
lis1.intSplitRemake(line1)
a=lis1.head.data
l=lis1.head.next.data
c=lis1.head.next.next.data
lis2=SingleLinkedList()
line1=input()
lis2.intSplitRemake(line1)
