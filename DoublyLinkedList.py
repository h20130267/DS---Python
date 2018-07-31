class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self,newNode):
        if self.head is None:
            self.head = newNode
            return
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def lengthDLL(self):
        if self.head is None:
            return 0
        currentNode = self.head
        count = 0
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            count += 1
        return count

    def printDLL(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                return
            print(currentNode.data)
            currentNode = currentNode.next



nodeOne = Node("Manoj")
nodeTwo = Node("Abhishek")
nodeThree = Node("Anish")

dll = DoublyLinkedList()
dll.insertAtStart(nodeOne)
dll.insertAtStart(nodeTwo)
dll.insertAtStart(nodeThree)

dll.printDLL()
print (dll.lengthDLL())             
