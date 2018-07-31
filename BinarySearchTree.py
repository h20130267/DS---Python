import random
from Queue import Queue
from Stack import Stack

class Node:
    def __init__(self,value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None
        self.balanceFactorli = []
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,currentNode):
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value)
            else:
                self._insert(value,currentNode.leftChild)
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert(value,currentNode.rightChild)
        else:
            print("Number Already in Tree !!!,{}".format(value))

    def printBST(self):
        if self.root == None:
            print("No Tree exists to print keys !!!")
        else:
            self._printBST(self.root)

    def _printBST(self,currentNode):
        if currentNode != None:
            self._printBST(currentNode.leftChild)
            print(currentNode.value)
            self._printBST(currentNode.rightChild)

    def sizeBST(self):
        if self.root == None:
            return 0
        else:
            return self._sizeBST(self.root,0)

    def _sizeBST(self,currentNode,currentSize):
        if currentNode == None:
            return currentSize
        leftChildHeight = self._sizeBST(currentNode.leftChild,currentSize+1)
        rightChildHeight = self._sizeBST(currentNode.rightChild,currentSize+1)
        return max(leftChildHeight,rightChildHeight)

    def inorderPredecessor(self,key):
        if self.root == None:
            print("No Tree to find Predecessor")
        targetNode = self.root
        while  (targetNode.value != key):
            if key < targetNode.value:
                targetNode = targetNode.leftChild
                if targetNode == None:
                    print("Entered key Not present in Tree. Pls Enter correct key")
                    return
            elif key > targetNode.value:
                targetNode = targetNode.rightChild
                if targetNode == None:
                    print("Entered key Not present in Tree. Pls Enter correct key")
                    return
            else:
                print("Key already Present !!!")
        #print (targetNode.value)
        if targetNode.leftChild != None:
            temp = targetNode.leftChild
            while temp.rightChild != None:
                temp = temp.rightChild
            return temp.value
        else:
            s = self.root
            store = None
            while (s.value != targetNode.value):
                if targetNode.value > s.value:
                    store = s.value
                    s = s.rightChild
                else:
                    s = s.leftChild
            if store != None:
                return store
            else:
                print("No Inorder Predecessor Possible !!!")

    def inorderSuccessor(self,key):
        if self.root == None:
            print("No Tree to find Successor")
        else:
            targetNode = self.root
            while (targetNode.value != key):
                if key > targetNode.value:
                    targetNode = targetNode.rightChild
                    if targetNode == None:
                        print("Entered key Not present in Tree. Pls Enter correct key")
                        return
                else:
                    targetNode = targetNode.leftChild
                    if targetNode == None:
                        print("Entered key Not present in Tree. Pls Enter correct key")
                        return
            #print(targetNode.value)
            if targetNode.rightChild != None:
                temp = targetNode.rightChild
                while temp.leftChild != None:
                    temp = temp.leftChild
                return temp.value
            else:
                s = self.root
                store = None
                while (targetNode.value != s.value):
                    if targetNode.value < s.value:
                        store = s
                        s = s.leftChild
                    else:
                        s = s.rightChild
                if store != None:
                    return store
                else:
                    print("No Inorder Successor Possible !!!")

    def balanceFactorOfNodeBST(self,key):
        p = self.root
        while key != p.value:
            if key < p.value:
                p = p.leftChild
                if (p is None):
                    print ("Key not in Tree. Enter Correct key !!!")
                    return 0
            if key > p.value:
                p = p.rightChild
                if (p is None):
                    print ("Key not in Tree. Enter Correct key !!!")
                    return 0
        #print(p.value)
        targetNode = p
        balanceFactor = self._balanceFactorOfNodeBST(targetNode,targetNode)
        print(balanceFactor)

    def _balanceFactorOfNodeBST(self,currentNode,keyNode):
        if currentNode == None:
            return 0
        else:
            leftChildHeight = self._balanceFactorOfNodeBST(currentNode.leftChild,keyNode)
            rightChildHeight = self._balanceFactorOfNodeBST(currentNode.rightChild,keyNode)
            balanceFactor = leftChildHeight - rightChildHeight
            #print(currentNode.value,balanceFactor)
            if currentNode != keyNode:
                return max(leftChildHeight,rightChildHeight)+1
            else:
                return balanceFactor

    def heightBT(self):
        if self.root == None:
            return 0
        else:
            p = self.root
            return self._heightBT(p)

    def _heightBT(self,currentNode):
        if currentNode == None:
            return 0
        else:
            leftChildHeight = self._heightBT(currentNode.leftChild)
            rightChildHeight = self._heightBT(currentNode.rightChild)
            return (max(leftChildHeight,rightChildHeight)+1)

    def deleteTree(self):
        if self.root == None:
            print("No tree exists to delete !!!")
        else:
            p = self.root
            self._deleteTree(p)

    def _deleteTree(self,currentNode):
        if currentNode == None:
            return
        else:
            self._deleteTree(currentNode.leftChild)
            self._deleteTree(currentNode.rightChild)
            print(currentNode.value)
            del currentNode
            #print(currentNode.value)

    def smallestKey(self):
        s = self.root
        while (s.leftChild != None):
            s = s.leftChild
        return s.value

    def largestKey(self):
        s = self.root
        while (s.rightChild != None):
            s = s.rightChild
        return s.value

    def sumOfAllNodes(self):
        if self.root == None:
            return 0
        else:
            p = self.root
            return self._sumOfAllNodes(p)

    def _sumOfAllNodes(self,currentNode):
        if currentNode == None:
            return 0
        else:
            leftsum = self._sumOfAllNodes(currentNode.leftChild)
            rightsum = self._sumOfAllNodes(currentNode.rightChild)
            return (leftsum + rightsum + currentNode.value)

    def balanceFactorsOfAllNodes(self):
        if self.root == 0:
            print("No Tree Exists !!!")
        else:
            p = self.root
            self._balanceFactorsOfAllNodes(p)

    def _balanceFactorsOfAllNodes(self,currentNode):
        if currentNode == None:
            return 0
        else:
            leftChildHeight = self._balanceFactorsOfAllNodes(currentNode.leftChild)
            rightChildHeight = self._balanceFactorsOfAllNodes(currentNode.rightChild)
            balanceFactor = leftChildHeight - rightChildHeight
            print ("Balance Factor of Node with key {} is {}".format(currentNode.value,balanceFactor))
            return (max(leftChildHeight,rightChildHeight)+1)

    def isAVLTree(self):
        if self.root == 0:
            print("No Tree Exists !!!")
            return True
        else:
            p = self.root
            li = [-1,0,1]
            self._isAVLTree(p)
            for bf in self.balanceFactorli:
                if bf not in li:
                    print (bf)
                    return False
            return True


    def _isAVLTree(self,currentNode):
        if currentNode == None:
            return 0
        else:
            leftChildHeight = self._isAVLTree(currentNode.leftChild)
            rightChildHeight = self._isAVLTree(currentNode.rightChild)
            balanceFactor = leftChildHeight - rightChildHeight
            self.balanceFactorli.append(balanceFactor)
            #print ("Balance Factor of Node with key {} is {}".format(currentNode.value,balanceFactor))
            return (max(leftChildHeight,rightChildHeight)+1)
    def verticalOrderTraversal(self):
        if self.root == None:
            print("No Tree exists for Vertical order Traversal")
            return 0
        else:
            dict = {}
            q = Queue()
            hdq =Queue()
            p = self.root
            #Horizontal Distance of root is 0
            hd = 0
            dict[hd] = [p.value]
            q.enQueue(p)
            hdq.enQueue(hd)
            while(1):
                cN = q.deQueue()#cN correspond to currentNode
                if cN is False:
                    break
                cNHorDis = hdq.deQueue()
                #print(cN.value,"--->",cNHorDis)
                #print(dict)
                if cN.leftChild != None:
                    if (cNHorDis-1) in dict.keys():
                        dict[cNHorDis-1].append(cN.leftChild.value)
                        #print(dict[cNHorDis-1])
                    else:
                        dict[cNHorDis-1] = [cN.leftChild.value]
                        #print(dict[cNHorDis-1])
                    q.enQueue(cN.leftChild)
                    hdq.enQueue(cNHorDis-1)
                if cN.rightChild != None:
                    if (cNHorDis+1) in dict.keys():
                        dict[cNHorDis+1].append(cN.rightChild.value)
                    else:
                        dict[cNHorDis+1] = [cN.rightChild.value]
                    q.enQueue(cN.rightChild)
                    hdq.enQueue(cNHorDis + 1)
            #print(list(dict.items()))
            minKey = min(dict.keys())
            maxKey = max(dict.keys())
            for key in range(minKey,maxKey+1):
                if key in dict.keys():
                    for ele in dict[key]:
                        print (ele)

    def levelOrderTravesalBT(self):
        if (self.root == None):
            print("No Tree present for InOrder Traversal")
        else:
            q = Queue()
            q.enQueue(self.root)
            while (1):
                currentNode = q.deQueue()
                if currentNode is False:
                    return
                print (currentNode.value)
                if currentNode.leftChild != None:
                    q.enQueue(currentNode.leftChild)
                if currentNode.rightChild != None:
                    q.enQueue(currentNode.rightChild)

    def zigzagLevelOrderTraversalBT(self):
        if self.root == None:
            print("No Tree exists to perform Zigzag tree Traversal !!!")
        else:
            s1 = Stack()
            s2 = Stack()
            p = self.root
            s1.push(p)
            while (s1.lengthStack() != 0 or s2.lengthStack() != 0):
                while s1.lengthStack() != 0:
                    currentNode = s1.pop()
                    print(currentNode.value)
                    if currentNode.leftChild != None:
                        s2.push(currentNode.leftChild)
                    if currentNode.rightChild != None:
                        s2.push(currentNode.rightChild)
                while s2.lengthStack() != 0:
                    currentNode = s2.pop()
                    print(currentNode.value)
                    if currentNode.rightChild != None:
                        s1.push(currentNode.rightChild)
                    if currentNode.leftChild != None:
                        s1.push(currentNode.leftChild)

    def topViewOfBinaryTree(self):
        if self.root == None:
            print("No Tree exists for top view")
            return 0
        else:
            dict = {}
            q = Queue()
            hdq =Queue()
            p = self.root
            #Horizontal Distance of root is 0
            hd = 0
            dict[hd] = [p.value]
            q.enQueue(p)
            hdq.enQueue(hd)
            while(1):
                cN = q.deQueue()#cN correspond to currentNode
                if cN is False:
                    break
                cNHorDis = hdq.deQueue()
                #print(cN.value,"--->",cNHorDis)
                #print(dict)
                if cN.leftChild != None:
                    if (cNHorDis-1) in dict.keys():
                        dict[cNHorDis-1].append(cN.leftChild.value)
                        #print(dict[cNHorDis-1])
                    else:
                        dict[cNHorDis-1] = [cN.leftChild.value]
                        #print(dict[cNHorDis-1])
                    q.enQueue(cN.leftChild)
                    hdq.enQueue(cNHorDis-1)
                if cN.rightChild != None:
                    if (cNHorDis+1) in dict.keys():
                        dict[cNHorDis+1].append(cN.rightChild.value)
                    else:
                        dict[cNHorDis+1] = [cN.rightChild.value]
                    q.enQueue(cN.rightChild)
                    hdq.enQueue(cNHorDis + 1)
            #print(list(dict.items()))
            minKey = min(dict.keys())
            maxKey = max(dict.keys())
            for key in range(minKey,maxKey+1):
                if key in dict.keys():
                    print(dict[key][0])

    def bottomViewOfBinaryTree(self):
        if self.root == None:
            print("No Tree exists for bottom View")
            return 0
        else:
            dict = {}
            q = Queue()
            hdq =Queue()
            p = self.root
            #Horizontal Distance of root is 0
            hd = 0
            dict[hd] = [p.value]
            q.enQueue(p)
            hdq.enQueue(hd)
            while(1):
                cN = q.deQueue()#cN correspond to currentNode
                if cN is False:
                    break
                cNHorDis = hdq.deQueue()
                #print(cN.value,"--->",cNHorDis)
                #print(dict)
                if cN.leftChild != None:
                    if (cNHorDis-1) in dict.keys():
                        dict[cNHorDis-1].append(cN.leftChild.value)
                        #print(dict[cNHorDis-1])
                    else:
                        dict[cNHorDis-1] = [cN.leftChild.value]
                        #print(dict[cNHorDis-1])
                    q.enQueue(cN.leftChild)
                    hdq.enQueue(cNHorDis-1)
                if cN.rightChild != None:
                    if (cNHorDis+1) in dict.keys():
                        dict[cNHorDis+1].append(cN.rightChild.value)
                    else:
                        dict[cNHorDis+1] = [cN.rightChild.value]
                    q.enQueue(cN.rightChild)
                    hdq.enQueue(cNHorDis + 1)
            #print(list(dict.items()))
            minKey = min(dict.keys())
            maxKey = max(dict.keys())
            for key in range(minKey,maxKey+1):
                if key in dict.keys():
                    print(dict[key].pop())

    def leftSideViewOfBinaryTree(self):
        if self.root == None:
            print("No Tree exists for left Side View !!!")
            return 0
        else:
            dict = {}
            q = Queue()
            levelq =Queue()
            p = self.root
            #Level of root is 0
            level = 0
            dict[level] = [p.value]
            q.enQueue(p)
            levelq.enQueue(level)
            while(1):
                cN = q.deQueue()#cN correspond to currentNode
                if cN is False:
                    break
                cNLevel = levelq.deQueue()
                if cN.leftChild != None:
                    if (cNLevel+1) in dict.keys():
                        dict[cNLevel+1].append(cN.leftChild.value)

                    else:
                        dict[cNLevel+1] = [cN.leftChild.value]

                    q.enQueue(cN.leftChild)
                    levelq.enQueue(cNLevel+1)
                if cN.rightChild != None:
                    if (cNLevel+1) in dict.keys():
                        dict[cNLevel+1].append(cN.rightChild.value)
                    else:
                        dict[cNLevel+1] = [cN.rightChild.value]
                    q.enQueue(cN.rightChild)
                    levelq.enQueue(cNLevel+1)

            minKey = min(dict.keys())
            maxKey = max(dict.keys())
            for key in range(minKey,maxKey+1):
                if key in dict.keys():
                    print (dict[key][0])

    def rightSideViewOfBinaryTree(self):
        if self.root == None:
            print("No Tree exists for right Side View !!!")
            return 0
        else:
            dict = {}
            q = Queue()
            levelq =Queue()
            p = self.root
            #Level of root is 0
            level = 0
            dict[level] = [p.value]
            q.enQueue(p)
            levelq.enQueue(level)
            while(1):
                cN = q.deQueue()#cN correspond to currentNode
                if cN is False:
                    break
                cNLevel = levelq.deQueue()
                if cN.leftChild != None:
                    if (cNLevel+1) in dict.keys():
                        dict[cNLevel+1].append(cN.leftChild.value)

                    else:
                        dict[cNLevel+1] = [cN.leftChild.value]

                    q.enQueue(cN.leftChild)
                    levelq.enQueue(cNLevel+1)
                if cN.rightChild != None:
                    if (cNLevel+1) in dict.keys():
                        dict[cNLevel+1].append(cN.rightChild.value)
                    else:
                        dict[cNLevel+1] = [cN.rightChild.value]
                    q.enQueue(cN.rightChild)
                    levelq.enQueue(cNLevel+1)

            minKey = min(dict.keys())
            maxKey = max(dict.keys())
            for key in range(minKey,maxKey+1):
                if key in dict.keys():
                    print (dict[key].pop())
"""
bst = BST()
li = [random.randint(1,400) for i in range(100)]
for key in li:
    bst.insert(key)
bst.printBST()
"""
bst = BST()
li = [50,16,90,14,40,15,10,5,35,32,36,37,78,100,75,82,81,85,79,87]
for key in li:
    bst.insert(key)
#bst.printBST()
print(bst.inorderPredecessor(35))
print(bst.smallestKey())
print(bst.largestKey())
print(bst.inorderSuccessor(100))
print(bst.heightBT())
print(bst.sizeBST())
#bst.deleteTree()
#bst.deleteTree()
#bst.deleteTree()
#print(bst.heightBT())
#bst.printBST()
print()
print(bst.sumOfAllNodes())
"""
x=0
for ele in li:
    x = x + ele
print(x)
"""
#bst.levelOrderTravesalBT()
#bst.zigzagLevelOrderTraversalBT()
bst.balanceFactorsOfAllNodes()
print(bst.isAVLTree())
print()
bst1 = BST()
li = [15,10,20,5,12,17,22,23,2,6,7]
for key in li:
    bst1.insert(key)
print("Checking Balancing Factors of all Keys............")
bst1.balanceFactorsOfAllNodes()
print("Checking if the given Tree is AVL Tree............")
print(bst1.isAVLTree())
print("Checking the Balance Factor of a given Key")
bst1.balanceFactorOfNodeBST(15)
print("Printing Vertical Order Traversal............")
bst1.verticalOrderTraversal()
print("Printing Top View Of Binary Tree............")
bst1.topViewOfBinaryTree()
print("Printing Bottom View Of Binary Tree............")
bst1.bottomViewOfBinaryTree()
print("Printing Left Side View Of Binary Tree............")
bst1.leftSideViewOfBinaryTree()
print("Printing Right Side View Of Binary Tree............")
bst1.rightSideViewOfBinaryTree()
