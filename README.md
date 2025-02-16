# Data-Structures
Portfolio project showcasing data structures implemented in multiple languages as a learning resource.

<!-- 


### 📌 Disclaimer: Readability Over Optimization  

This repository prioritizes **clarity and readability** over micro-optimizations. The goal is to provide a well-structured and easy-to-understand implementation of data structures, ensuring that the concepts are clear rather than focusing on minor performance gains.  

For example, consider the following two approaches to initializing a linked list:  

#### ✅ Readable & Explicit (Preferred for Clarity)
```python
class LinkedList:
    def __init__(self, data=None):
        self.head = None  # Explicitly initializing head
        if data:
            self.head = Node(data)
```

#### ⚡ Slightly Optimized 
```python
class LinkedList:
    def __init__(self, data=None):
        # No redundant initialization
        if data:
            self.head = Node(data)
        else:
            self.head = None
```


While both versions work the same way, the first approach is preferred in this repository as it ensures **consistency and clarity**.  

> **Note:** In performance-critical applications, optimizations may take priority. However, for a learning-focused showcase like this, **understanding the concepts matters more than minor efficiency improvements**. -->