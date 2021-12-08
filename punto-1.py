class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
#creacion de len(), putFront(n) y sort()(después)
#putFront es sacar de la posición n y poner al inicio
class LinkedList: 
    def __init__ (self ):
        self.head = None

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
        print() #espacio en blanco 

    def insert(self,head,data): 
        if head == None:
            nextNode = Node(data)
            return nextNode
        elif head.next == None:
            nextNode_ = Node(data)
            head.next = nextNode_
            return head
        else:
            self.insert(head.next, data)
        return head
        
    def popFront(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            popped = self.head
            self.head = None
            return popped
        else:
            popped = self.head
            self.head = self.head.next
            return popped

    def len (self, head ):
        x = head
        count = 0
        while (x):
            count +=1
            x = x.next
        return count
        
    def toLL (self,p,n):
        self.head = None
        for i in range (0,n,1):
            self.head = self.insert(self.head, p[i])

          #U.U  
            
#tocar, pero poquito  :D
#hay que mover la asignación de las variables locales dentro de los casos
global jugadores
jugadores = LinkedList()

global cartas
cartas = LinkedList()



t = input() #Numero casos de prueba

#hay que crear un bucle para todo esto de t casos

n, k = map(int,input().split())# N = Cantidad de cartas y K = Cantidad de jugadores
headCartas = None
headJugadores = None

#inserta en la lista enlazada tal que jugadores = 1 -> 2 -> ... -> k
for i in range(k):
    headJugadores = jugadores.insert(headJugadores, i+1)

jugadores.len(headJugadores)

P = input().split()

#inserta la lista P_i a la lista de las cartas(pero solo recibe n cartas)

headCartas = cartas.toLL(P,n) #Mete la lista de cartas en la linked list
#for i in range(n):    
 #   headCartas = cartas.insert(headCartas, P[i])



#Primero hay que completar la clase de LinkedList para ir comprobando los métodos de baraja


#baraja va a ser una lista enlazada con dos datos, el jugador y su puntaje, por eso no es 
# una LinkedList (porque posee "dos datas") pero si posee todas sus características
class Deck(LinkedList):
    score = 0
    #un bucle según los jugadores, asocia los jugadores con la primera carta a la izquierda
    def __init__(self, jugadores, cartas):
        self.player = jugadores.popFront()
        self.takeCard(cartas)
        super(self)
    #un bucle según las cartas que hayan sobrado, para ese bucle necesitamos validar varias veces el número
    #de cartas y de jugadores
    def takeCard(self, cartas):
        if cartas.data() != None:
            self.score += cartas.popFront()

    def nextRound(self):
        if cartas.len(headCartas) != 0:
            self.takeCard(self.cartas)
    def insert(self, head, jugador, cartas):
        super().insert(head, jugador)
        self.takeCard(cartas)

barajas = Deck(jugadores, cartas)

headBaraja = None
for i in range(jugadores.len(headJugadores)):
    headBaraja = Deck.insert(headBaraja, jugadores.popFront(), cartas.popFront())

    



        
    
    



