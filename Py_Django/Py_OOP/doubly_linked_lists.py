class Dnode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Dlist:
    def __init__(self, value):
        node = Dnode(value)
        self.head = node
