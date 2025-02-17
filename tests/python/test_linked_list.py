import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../python')))

from SinglyLinkedList import SinglyLinkedList  # type: ignore

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SinglyLinkedList()

    def test_append(self):
        self.ll.append(1)
        self.assertEqual(str(self.ll), "( 1 )")
        self.ll.append(2)
        self.assertEqual(str(self.ll), "( 1 ) -> ( 2 )")
        self.ll.append(3)
        self.assertEqual(str(self.ll), "( 1 ) -> ( 2 ) -> ( 3 )")

    def test_get(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)
        self.assertIsNone(self.ll.get(3))

    def test_delete(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.delete(1)
        self.assertEqual(str(self.ll), "( 1 ) -> ( 3 )")
        self.ll.delete(0)
        self.assertEqual(str(self.ll), "( 3 )")
        self.ll.delete(0)
        self.assertEqual(str(self.ll), "Empty Linked List")
        self.ll.append(4)
        self.ll.append(5)
        self.ll.delete(1)
        self.assertEqual(str(self.ll), "( 4 )")
        self.ll.delete(0)
        self.assertEqual(str(self.ll), "Empty Linked List")

if __name__ == "__main__":
    unittest.main()
