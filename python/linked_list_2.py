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
        output = f"{self.head.data}"
        while True:
            if node.next is None:
                break
            node = node.next
            output += f" -> {node.data}"
        return output
    
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
    def delete(self):
        pass
    
    

if __name__ == "__main__":
    # Create a Linked List with initial value of 5
    ll = LinkedList()
    
    ll.append(10)
    ll.append(8)
    ll.append(7)
    print(ll)

    print(f"Head Element: {ll.get(0)}")
    print(f"Second Element: {ll.get(1)}")
    print(f"Third Element: {ll.get( 2)}")
    print(f"Fourth Element: {ll.get(3)}")
    # print("-" * 25)
    
    # print("Link List Visualization:\n")
    
    # ll.delete(0)
    # print("Element 0 is removed:\n", ll, "\n")
    
    # ll.delete(2)
    # print("Element 2 is removed:\n", ll, "\n")
    
    # ll.delete(10)
    # print("Element 10 is removed:\n", ll, "\n")
