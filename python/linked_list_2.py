class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Empty Linked List"

        node = self.head
        output = [self.head.data]
        while node.next:
            node = node.next
            output.append(node.data)
        return " -> ".join([f"( {x} )" for x in output])

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            last_node = self.head

            # in loop
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def get(self, index):
        if self.head is None:
            return None

        node = self.head

        for i in range(index):
            if node.next is None:
                return None
            node = node.next

        # while True:
        #     if i == index:
        #         break
        #     if node.next is None:
        #         return None

        #     node = node.next
        #     i += 1

        return node.data

    def delete(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next or None
            return

        node = self.head

        # while True:
        #     if i == index-1:
        #         break
        #     if node.next is None:
        #         return None

        #     node = node.next
        #     i += 1

        for _ in range(index - 1):
            if node.next is None:
                return None

            node = node.next

        # Explanation
        # there are 3 nodes we think about:
        # prev node -> node to delete -> next node
        # we try to link prev node to next note, ignoring the node to delete
        # if the next node is not none, it works. otherwise we link prev node to None
        # node.next = node.next.next

        if node.next is not None:
            # node is 100% not none (ensured in the loop)
            # node.next might be None, so we might not access node.next.next
            # so we check it.
            node.next = node.next.next
        else:
            node.next = None


if __name__ == "__main__":
    # Create a Linked List with initial value of 5
    ll = LinkedList()

    ll.append(10)
    ll.append(9)
    ll.append(8)
    ll.append(7)
    print(ll)

    # print(f"Head Element: {ll.get(0)}")
    # print(f"Second Element: {ll.get(1)}")
    # print(f"Third Element: {ll.get( 2)}")
    # print(f"Fourth Element: {ll.get(3)}")
    # print("-" * 25)

    # print("Link List Visualization:\n")

    ll.delete(0)
    print("Element 0 is removed:", ll)

    ll.delete(0)
    print("Element 0 is removed:", ll)

    # ll.delete(10)
    # print("Element 10 is removed:\n", ll, "\n")
