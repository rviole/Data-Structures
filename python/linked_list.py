class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data=data)

    def __str__(self):
        node_sequence = f"HEAD ( {self.head.data} )"
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            node_sequence += f" -> ( {last_node.data} )"
        node_sequence += " TAIL"
        
        return node_sequence

    def append(self, data):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        # Assign a new node after the last node
        last_node.next = Node(data)

    def get(self, index):
        last_node = self.head
        for _ in range(index):
            # Tail's next is None
            # So if we exceed the length of the list, return None
            if not last_node.next:
                return None
            last_node = last_node.next
        return last_node.data
    

if __name__ == "__main__":
    # Create a Linked List with initial value of 5
    ll = LinkedList(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)

    print(f"\nHead Element: {ll.get(0)}")
    print(f"Second Element: {ll.get(1)}")
    print(f"Third Element: {ll.get(2)}")
    print(f"Fourth Element: {ll.get(3)}")
    print("-"*25)
    print("Link List Visualization:\n")
    print(ll, "\n")
