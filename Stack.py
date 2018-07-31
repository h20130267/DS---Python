class Stack:
    def __init__(self):
        self.list = []
        self.top = -1

    def push(self,data):
        self.top += 1
        self.list.insert(self.top,data)


    def pop(self):
        if (self.top == -1):
            print("Invalid to perform Pop operation !!!")
            return False
        top = self.top
        self.top -= 1
        return self.list[top]

    def printStack(self):
        if (self.top == -1):
            print ("Empty Stack")
            return False
        else:
            count = 0
            while(count <= self.top):
                print(self.list[count])
                count += 1
            return True

    def printStackReverse(self):
        if (self.top == -1):
            print ("Empty Stack")
            return False
        else:
            dec = self.top
            while True:
                if (dec < 0):
                    break
                print (self.list[dec])
                dec -= 1
            return True

    def lengthStack(self):
        return self.top+1
"""
s = Stack()
s.push(1)
s.push(2)
s.push(3)

s.printStack()
print(s.lengthStack())
print()
s.pop()
s.printStackReverse()
print(s.lengthStack())
print()
"""
