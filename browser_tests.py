import unittest
from browser_history import *

class TestBrowserHistory(unittest.TestCase):
    def test_push(self):
        stack1 = Stack()
        stack1.push("test_item")
        self.assertEqual(stack1.items_list[-1], "test_item")

    def test_dequeue(self):
        stack1 = Stack()
        stack1.push("test_item1")
        stack1.pop()
        listAfterDequeue = []
        self.assertEqual(stack1.items_list, listAfterDequeue)

    def test_peek(self):
        stack1 = Stack()
        stack1.push("test_item1")
        anotherList = ["test_item1"]
        self.assertEqual(stack1.peek(), anotherList)

if __name__ == "__main__":
    unittest.main()