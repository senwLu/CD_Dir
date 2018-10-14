class Snode():
    def __init__(self, value):
        self.value = value
        self.next = None


class SList():
    def __init__(self, value):
        node = Snode(value)
        self.head = node

    def addNode(self, value):
        node = Snode(value)
        # runner starts at the beginning of linked list, so runner => self.head
        runner = self.head
        # while runner.next is not None, keep running down the list
        while runner.next != None:
            runner = runner.next
        # once runner reaches last node, connect last node to new node
        runner.next = node
        return self

    def printAllValues(self, text):
        runner = self.head
        print(text)
        # while runner.next is not None, print value the runner is currently on and its next value pointer
        # if next is None, runner does not print value of current node and breaks out of while loop
        while runner.next != None:
            print(runner.value, runner.next)
            runner = runner.next
        # printing value of last node
        print(runner.value, runner.next)

    def removeNode(self, value):
        runner = self.head

        # check if value to be removed is at the start(head) of linked list
        if value == runner.value:
            # if value to be removed is head of linked list, set pointer to next value as head of list
            self.head = runner.next
        else:
            # if node value in front of current node is not the value to be removed, keep traversing down the list
            while runner.next.value != value:
                runner = runner.next

            # ## if next node value is equal to the value to be removed, break out of while loop ##

            runner.next = runner.next.next

    def insertNode(self, value, index):
        insertNode = Snode(value)
        length = 0
        runner = self.head
        slow_runner = None

        # check if insertion index is at start(head) of linked list
        if index == 0:
            insertNode.next = runner
            self.head = insertNode

        else:

            while length != index:
                slow_runner = runner
                runner = runner.next
                length += 1

            insertNode.next = runner
            slow_runner.next = insertNode


# creating  an instance of list with first node having the value of 5
list = SList(5)
list.addNode(3).addNode(1)
list.printAllValues('Attempt 1')

list.insertNode(7, 2)
list.printAllValues('Insert attempt 1')
