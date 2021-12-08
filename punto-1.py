class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.head = None
#creacion de len(), putFront(n) y sort()(después)
#putFront es sacar de la posición n y poner al inicio
class LinkedList: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

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
        
    def popFront(self, head):
        if head != None:
            return None
            
        r = head.data
        head = head.next
        print ('popfronted ', r)
        return head

    def len (self, head ):
        x = head
        count = 0
        while (x):
            count +=1
            x = x.next
        
            
            
            
#tocar, pero poquito  :D
#hay que mover la asignación de las variables locales dentro de los casos
global jugadores
jugadores = LinkedList()

global cartas
cartas = LinkedList()



t = input() #Numero casos de prueba

#hay que crear un bucle para todo esto de t casos

n, k = map(int,input().split())# N = Cantidad de cartas y K = Cantidad de jugadores
head = None
print(n, k)
#inserta en la lista enlazada tal que jugadores = 1 -> 2 -> ... -> k
for i in range(k):
    head = jugadores.insert(head, i+1)

#Primero hay que completar la clase de LinkedList para ir comprobando los métodos de baraja


#baraja va a ser una lista enlazada con dos datos, el jugador y su puntaje, por eso no es 
#una LinkedList (porque posee "dos datas") pero si posee todas sus características
class Baraja(LinkedList):
    score = 0
    #un bucle según los jugadores, asocia los jugadores con la primera carta a la izquierda
    def __init__(self, player, cards):
        self.player = jugadores.popFront()
        if cartas.data() != None:
            self.score += cartas.popFront()
    #un bucle según las cartas que hayan sobrado, para ese bucle necesitamos validar varias veces el número
    #de cartas y de jugadores
    def reChoose(nextRound):
    #los nombres de lo que hay en reChoose son muy confusos, hay que cambiarlos
        while (cartas.len()-- != 0):
            nextRound = Baraja(nextRound.player, nextRound.cartas)
    



