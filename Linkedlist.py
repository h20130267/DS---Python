from Stack import Stack

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAtStart(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtPos(self,newNode,pos):
        if (pos > self.length()):
            print ("Invalid Insertion !!!")
            return False
        elif (pos == self.length()):
            self.insertAtEnd(newNode)
            return True
        elif (pos == 0):
            self.insertAtStart(newNode)
            return True
        else:
            currentNode = self.head
            #print (currentNode.data)
            count = 0
            while True:
                if (count >= pos):
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                #print(previousNode.data)
                count+=1
            newNode.next = currentNode
            previousNode.next = newNode
            print("Insertion Successful")
            return True

    def deleteAtPos(self,pos):
        if (pos == 0):
            currentNode = self.head
            self.head = currentNode.next
            del currentNode
            return True
        elif (pos >= self.length()):
            print ("Invalid Deletion of Node !!!")
        else:
            currentNode = self.head
            count = 0
            while True:
                if (count >= pos):
                    break
                count+=1
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = currentNode.next
            del currentNode

    def length(self):
        currentNode = self.head
        count = 0
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            count+=1
        return count

    def printLL(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print (currentNode.data)
            currentNode = currentNode.next

    def reverseLL(self):
        s = Stack()
        currentNode = self.head
        prev = self.head
        while True:
            if currentNode is None:
                break
            #print(currentNode)
            s.push(currentNode)
            currentNode = currentNode.next
            #print(currentNode)
        self.head.next = None
        self.head = s.pop()
        #print(self.head)
        currentNode = self.head
        while True:
            if currentNode is prev:
                return
            nextNode = s.pop()
            #print(nextNode)
            currentNode.next = nextNode
            currentNode = nextNode


"""
ll = LinkedList()
nodeOne = Node("Manoj")
ll.insertAtEnd(nodeOne)

nodeTwo = Node("Arvind")
ll.insertAtEnd(nodeTwo)

nodeThree = Node("Anish")
ll.insertAtEnd(nodeThree)

nodeFour = Node("Kiriti")
ll.insertAtStart(nodeFour)

nodeFive = Node("Avinash")
ll.insertAtPos(nodeFive,3)
ll.printLL()
print (ll.length())
print()
ll.deleteAtPos(5)
ll.printLL()
print (ll.length())
print()
"""
