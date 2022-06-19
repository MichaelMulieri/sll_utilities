class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self, head):
        self.head = head

    def addFront(self, val):
        new_node = Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node

    """def display(self):
        runner = self.head
        while runner:
            print(runner.val)
            runner = runner.next
        return self"""

    def contains(self, val):
        runner = self.head
        while runner:
            if runner.val == val:
                return True
            runner=runner.next
        return False

    def length(self):
        runner = self.head
        length = 0
        while runner:
            length += 1
            runner = runner.next
        return length

    def display(self):
        runner = self.head
        str =''
        while runner:
            str+=f'{runner.val}'
            runner=runner.next
        return str




list = SLL(Node(50))
print(list.head.val)
list.addFront(40)
list.addFront(30)
list.display()
print(list.contains(50))
print(list.length())