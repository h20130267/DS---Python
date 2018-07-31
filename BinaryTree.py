class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self,rootObj):
        self.key = rootObj

    def getRootVal(self):
        return self.key

b = BinaryTree(2)
b.insertLeft(4)
b.insertRight(6)
b.leftChild.insertLeft(2)
b.leftChild.insertRight(4)
b.leftChild.rightChild.insertLeft(3)
b.leftChild.rightChild.insertRight(9)
b.rightChild.insertLeft(5)
b.rightChild.insertRight(6)


"""
print(b.getRootVal())

print(b.getLeftChild().key)
print(b.getRightChild().key)

print(b.leftChild.getLeftChild().key)
print(b.leftChild.getRightChild().key)
print(b.rightChild.getLeftChild().key)
print(b.rightChild.getRightChild().key)

print(b.leftChild.getLeftChild().leftChild)
print(b.leftChild.getLeftChild().rightChild)
print(b.leftChild.getRightChild().leftChild.key)
print(b.leftChild.getRightChild().rightChild.key)
print(b.rightChild.getLeftChild().leftChild)
print(b.rightChild.getLeftChild().rightChild)
print(b.rightChild.getRightChild().leftChild)
print(b.rightChild.getRightChild().rightChild)
"""

def preOrderTraversal(tree):
    if tree is not None:
        print(tree.getRootVal())
        preOrderTraversal(tree.getLeftChild())
        preOrderTraversal(tree.getRightChild())

def inOrderTraversal(tree):
    if tree is not None:
        inOrderTraversal(tree.getLeftChild())
        print(tree.getRootVal())
        inOrderTraversal(tree.getRightChild())

def postOrderTraversal(tree):
    if tree is not None:
        postOrderTraversal(tree.getLeftChild())
        postOrderTraversal(tree.getRightChild())
        print(tree.getRootVal())


preOrderTraversal(b)
print()
inOrderTraversal(b)
print()
postOrderTraversal(b)
