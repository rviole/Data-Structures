
class Node:
    """A node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return "Empty Linked List"

        node = self.head
        output = [self.head.data]
        while node.next:
            node = node.next
            output.append(node.data)
        return " -> ".join([f"( {x} )" for x in output])

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        if self.head is None:
            # If the linked list is empty, the first element is both head and tail
            self.head = Node(data)
            self.tail = self.head
        else:
            # Add the new node at the end and update the tail
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def get(self, index):
        """Get the data of the node at the given index. Return None if index is out of bounds."""
        if self.head is None:
            return None

        node = self.head
        for _ in range(index):
            if node.next is None:
                return None
            node = node.next

        return node.data

    def delete(self, index):
        """Delete the node at the given index."""
        if self.head is None:
            return

        if index == 0:
            # Remove the head node
            self.head = self.head.next or None
            return

        previous = self.head
        for _ in range(index - 1):
            if previous.next is None:
                return None
            previous = previous.next

        if previous.next is not None:
            # Link the previous node to the next node, skipping the node to delete
            previous.next = previous.next.next
            # If we removed the last node, update the tail
            if previous.next is None:
                self.tail = previous
        else:
            previous.next = None
            self.tail = previous


if __name__ == "__main__":
    # Example usage of the LinkedList class
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(9)
    ll.append(8)
    ll.append(6)
    ll.append(5)
    ll.append(4)
    ll.append(2)
    ll.append(1)
    print(ll)

    ll.delete(0)
    print("Element 0 is removed:", ll)
    print(ll.head.data, ll.tail.data)
    
    ll.delete(4)
    print("Element 4 is removed:", ll)
    print(ll.head.data, ll.tail.data)
    
    ll.delete(5)
    print("Element 5 is removed:", ll)
    print(ll.head.data, ll.tail.data)
