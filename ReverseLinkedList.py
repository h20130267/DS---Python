from Linkedlist import Node,LinkedList

ll = LinkedList()
nodeOne = Node("Manoj")
ll.insertAtStart(nodeOne)
nodeTwo = Node("Amit")
ll.insertAtEnd(nodeTwo)
nodeThree = Node("Anish")
ll.insertAtEnd(nodeThree)
nodeFour= Node("Avinash")
ll.insertAtEnd(nodeFour)

ll.printLL()
print()

ll.reverseLL()
ll.printLL()
print()

nodeFive= Node("Arvind")
ll.insertAtEnd(nodeFive)

ll.printLL()
print()

ll.reverseLL()
ll.printLL()
