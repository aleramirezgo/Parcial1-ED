class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
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
            nextNode = Node(data)
            head.next = nextNode
            return head
        else:
            self.insert(head.next, data)
	

t = input() #Numero casos de prueba
nAndK= input().split()
n = int(nAndK[0]) # N = Cantidad de cartas y K = Cantidad de jugadores
k = int(nAndK[1])
jugadores = LinkedList()
head=None
print(n, k)
for i in range(n+1):
    head = jugadores.insert(head, i+1)
jugadores.display(head)

# for i in range(T):
#     data=int(input())
#     head=mylist.insert(head,data)    
#     mylist.display(head); 
      
