# 反向输出一个链表。

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, head = None) -> None:
        self.head = head
    
    def append(self, next):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = next
        else:
            self.head = next
    
    def delete(self, node):
        current = self.head
        prev = None
        if current.value == node.value:
            self.head = current.next
        else:
            while current:
                if current.value == node.value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None
    
    def insert(self, node, position = 0):
        if position == 0:
            node.next, self.head = self.head, node
        else:
            current = self.head
            index = 0
            while current:
                if index + 1 == position:
                    node.next, current.next = current.next, node
                    return
                else:
                    index += 1
                    current = current.next

    def showList(self) -> None:
        outputArray = []
        current = self.head
        while current:
            outputArray.append(current.value)
            current = current.next
        print(outputArray)

    def reserve(self) -> None:
        current = self.head
        prev = None
        next = current.next
        while current:
            self.head = current
            current.next = prev
            prev = current
            current = next
            next = next.next if next else None
           
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

link = LinkList()
link.append(node1)
link.append(node2)
link.append(node3)
link.append(node4)
link.append(node5)
link.append(node6)
link.append(node7)

link.reserve()

link.showList()
