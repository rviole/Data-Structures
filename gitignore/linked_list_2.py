class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
            # if the linked list is empty, the first element is both head and tail
            self.head = Node(data)
            self.tail = self.head
        else:
            # last_node = self.head

            # # in loop
            # while last_node.next:
            #     last_node = last_node.next

            # last_node.next = self.tail = Node(data)
            
            self.tail.next = Node(data)
            self.tail = self.tail.next            

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

        previous = self.head

        # while True:
        #     if i == index-1:
        #         break
        #     if node.next is None:
        #         return None

        #     node = node.next
        #     i += 1

        for _ in range(index - 1):
            if previous.next is None:
                return None

            previous = previous.next
            

        # Explanation
        # there are 3 nodes we think about:
        # prev node -> node to delete -> next node
        # we try to link prev node to next note, ignoring the node to delete
        # if the next node is not none, it works. otherwise we link prev node to None
        # node.next = node.next.next

        if previous.next is not None:
            # node is 100% not none (ensured in the loop)
            # node.next might be None, so we might not access node.next.next
            # so we check it.
            previous.next = previous.next.next
            
            # if we removed the last node, previous one becomes the tail
            if previous.next is None:
                self.tail = previous            
        else:
            previous.next = None
            self.tail = previous


if __name__ == "__main__":
    # Create a Linked List with initial value of 5
    ll = LinkedList()

    ll.append(10)
    ll.append(9)
    ll.append(8)
    ll.append(6)
    ll.append(5)
    ll.append(4)
    ll.append(2)
    ll.append(1)
    print(ll)

    # print(f"Head Element: {ll.get(0)}")
    # print(f"Second Element: {ll.get(1)}")
    # print(f"Third Element: {ll.get( 2)}")
    # print(f"Fourth Element: {ll.get(3)}")
    # print("-" * 25)

    # print("Link List Visualization:\n")

    ll.delete(0)
    print("Element 0 is removed:", ll)
    print(ll.head.data, ll.tail.data)
    
    ll.delete(4)
    print("Element 0 is removed:", ll)
    print(ll.head.data, ll.tail.data)
    
    ll.delete(5)
    print("Element 0 is removed:", ll)
    print(ll.head.data, ll.tail.data)

    # ll.delete(10)
    # print("Element 10 is removed:\n", ll, "\n")
