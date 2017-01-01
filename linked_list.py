class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = self.head

    def add_element(self, data):
        if self.head.value is None:
            self.head.value = data
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next

    def set_element(self, index, data):
        current = self.index(index)
        current.value = data

    def index(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def size(self):
        cnt = 0
        current = self.head
        while current is not None:
            cnt += 1
            current = current.next
        return cnt

    def remove(self, index):
        if index != 0:
            prev = self.index(index - 1)
            prev.next = prev.next.next
        else:
            self.head = self.head.next

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
        if index != 0:
            prev = self.index(index - 1)
            prev.next = Node(data, prev.next)
        else:
            self.add_first(data)

    def add_first(self, data):
        self.head = Node(data, self.head)

    def add_list(self, lst):
        for item in lst:
            self.tail.next = Node(item, None)
            self.tail = self.tail.next

    def add_linked_list(self, llist):
        self.tail.next = llist.head
        self.tail = llist.tail

    def ll_from_to(self, start_index, end_index):
        ll = LinkedList()
        current = self.index(start_index)
        for i in range(end_index - start_index):
            ll.add_element(current.value)
            current = current.next
        return ll

    def pop(self):
        before_last = self.index(self.size() - 2)
        last = before_last.next.value
        before_last.next = None
        self.tail = before_last
        return last

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

class Node:
    def __init__(self, value, nxt_node):
        self.value = value
        self.next = nxt_node


def main():


if __name__ == "__main__":
    main()

