class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data=data)

    def __str__(self):
        if self.head is None:
            return "HEAD ()"
        node_sequence = f"HEAD ( {self.head.data} )"
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
            node_sequence += f" -> ( {last_node.data} )"
        node_sequence += " TAIL"

        return node_sequence

    def append(self, data):
        if self.head is None:
            self.head = Node(data=data)
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = Node(data)

    def get(self, index):
        node = self.head
        idx = 0
        
        out = None
        while idx <= index:
            out = node.data
            if node.next is not None:
                node = node.next
            idx += 1
            
        return out

    def delete(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return
        
        prev = self.head
        for idx in range(index-1):
            if prev.next is None:
                return
            
            prev = prev.next        
        
        if prev.next:
            next_node = prev.next.next
            if next_node:
                prev.next = next_node
            else:
                prev.next = None
        
    

if __name__ == "__main__":
    # Create a Linked List with initial value of 5
    ll = LinkedList(1)
    # print(ll, "\n")
    ll.append(0)
    ll.append(7)
    ll.append(8)

    print(f"\nHead Element: {ll.get(0)}")
    print(f"Second Element: {ll.get(1)}")
    print(f"Third Element: {ll.get(2)}")
    print(f"Fourth Element: {ll.get(3)}")
    print("-" * 25)
    print("Link List Visualization:\n")
    print(ll, "\n")
    # ll.delete(0)
    # ll.delete(3)
    # print(ll, "\n")
    # ll.delete(10)
    # print(ll, "\n")
