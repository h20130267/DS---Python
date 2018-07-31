#Min Heap ---->Priority Queue ----->BinaryHeap
class MinBinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,key):
        self.heapList.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while (i//2) > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    def delMin(self):
        if self.currentSize > 0 :
            retVal = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.heapList.pop()
            self.currentSize -= 1
            self.percDown(1)
            return retVal

    def percDown(self,i):
        while (2*i) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def minChild(self,i):
        if (2*i +1) > self.currentSize:
            return 2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i + 1]:
                return 2*i
            else:
                return 2*i + 1

    def buildHeap(self,newList):
        nlSize = len(newList)
        print(nlSize)
        self.heapList = self.heapList + newList
        print (self.heapList)
        self.currentSize = self.currentSize+nlSize
        i = self.currentSize
        while i > 0:
            self.percDown(i)
            i -= 1

    def findMin(self):
        return self.heapList[1]

    def isEmpty(self):
        if self.currentSize > 0:
            return True
        else:
            return False

    def size(self):
        return self.currentSize



b = MinBinHeap()
list = [9,8,7,6,5]
b.buildHeap(list)
print (b.heapList)
print ()
b.insert(3)
print (b.heapList)
print(b.delMin())
print(b.heapList)
print(b.delMin())
print(b.heapList)
b.buildHeap([0,4,2,1,6,9,5])
print(b.heapList)
