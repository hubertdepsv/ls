class LinkedList:
    def __init__(self):
        pass

    def to_list(self):
        pass
    def from_list(self):
        pass

class Element:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def is_tail(self):
        return True if self.next is None else False