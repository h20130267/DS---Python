from Stack import Stack

class Queue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enQueue(self,data):
        self.instack.push(data)

    def deQueue(self):
        if (self.outstack.lengthStack() == 0):
            lenIN=self.instack.lengthStack()
            if (lenIN == 0):
                #print ("DeQueue operation invalid !!!")
                return False
            count = 0
            while True:
                if (count >= lenIN):
                    break
                self.outstack.push(self.instack.pop())
                count += 1
            return self.outstack.pop()
        return self.outstack.pop()

    def printQueue(self):
        if (self.outstack.lengthStack() == 0):
            self.instack.printStack()
            return
        self.outstack.printStackReverse()
        if (self.instack.lengthStack() != 0):
            self.instack.printStack()
        return

    def isEmpty(self):
        if (self.instack.lengthStack == 0 and self.outstack.lengthStack == 0):
            return True
        else:
            return False
"""
q = Queue()
q.enQueue("Manoj")
q.enQueue("Anish")
q.enQueue("Arvind")
q.enQueue("Abhay")
q.printQueue()
print()
q.deQueue()
q.printQueue()
print()
q.enQueue("Abhinay")
q.enQueue("Shreyas")
q.printQueue()
print()

q.deQueue()
q.printQueue()
print()
"""
