class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLLNode(None, None, None)
        self.tail = self.head

    def add_element(self, data):
        if self.head.value is None:
            self.head.value = data
        else:
            self.tail.next = DoubleLLNode(data, None, None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def set_element(self, index, data):
        pass

    def index(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def size(self):
        current = self.head
        counter = 0
        while current is not None:
            current = current.next
            counter += 1
        return counter

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.index(index)
            curr.prev.next = curr.next

    def pprint(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def to_list(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst

    def add_at_index(self, index, data):
        if index == 0:
            self.add_first(data)
        else:
            curr = self.index(index)
            curr.prev.next = DoubleLLNode(data, curr, curr.prev)

    def add_first(self, data):
        self.head.prev = Node(data, self.head, None)
        self.head = self.head.prev

    def add_list(self, lst):
        for item in lst:
            self.tail.next = DoubleLLNode(item, None, self.tail)
            self.tail = self.tail.next

    def add_linked_list(self, otherll):
        self.tail.next = otherll.head
        otherll.head.prev = self.tail
        self.tail = otherll.tail

    def ll_from_to(self, start_index, end_index):
        ll = LinkedList()
        current = self.index(start_index)
        for i in range(end_index - start_index):
            ll.add_element(current.value)
            current = current.next
        return ll

    def pop(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def reduce_to_unique(self):
        unique_values = set()
        unique_ll = LinkedList()
        current = self.head
        for i in range(self.size()):
            if current.value not in unique_values:
                unique_ll.add_element(current.value)
                unique_values.add(current.value)
            current = current.next
        return unique_ll


class DoubleLLNode:
    def __init__(self, value, next_node, prev_node):
        self.value = value
        self.prev = prev_node
        self.next = next_node

def main():
    pass

if __name__ == "__main__":
    main()