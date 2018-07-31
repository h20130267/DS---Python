class MaxBinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,key):
        self.heapList.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while (i//2)>0:
            if self.heapList[i] > self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    def delMax(self):
        if self.currentSize > 0:
            retVal = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.heapList.pop()
            self.currentSize -= 1
            self.percDown(1)
            return retVal

    def percDown(self,i):
        while (2*i) <= self.currentSize:
            mc = self.maxChild(i)
            temp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = temp
            i = mc

    def maxChild(self,i):
        if (2*i + 1) > self.currentSize:
            return 2*i
        else:
            if self.heapList[2*i] > self.heapList[2*i + 1]:
                return 2*i
            else:
                return 2*i + 1

    def buildHeap(self,newList):
        nlSize = len(newList)
        self.heapList += newList
        self.currentSize += nlSize
        i = self.currentSize
        while i > 0:
            self.percDown(i)
            i -= 1

    def findMax(self):
        return self.heapList[1]

    def isEmpty(self):
        if self.currentSize > 0:
            return False
        else:
            return True
    def size(self):
        return self.currentSize



        
b = MaxBinHeap()
list = [1,2,4,5,6,7,8,9,0]
b.buildHeap(list)
print (b.heapList)
print ()
b.insert(3)
print (b.heapList)
print(b.delMax())
print(b.heapList)
print(b.delMax())
print(b.heapList)
b.buildHeap([li for li in range(10,25)])
print(b.heapList)
