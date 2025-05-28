import unittest
from library_reservation import *

class TestLibraryReservation(unittest.TestCase):
    def test_enqueue(self):
        queue1 = Queue()
        queue1.enqueue("test_item")
        self.assertEqual(queue1.items_list[-1], "test_item")

    def test_dequeue(self):
        queue1 = Queue()
        queue1.enqueue("test_item1")
        queue1.dequeue()
        listAfterDequeue = []
        self.assertEqual(queue1.items_list, listAfterDequeue)

    def test_peek(self):
        queue1 = Queue()
        queue1.enqueue("test_item1")
        anotherList = ["test_item1"]
        self.assertEqual(queue1.peek(), anotherList)

if __name__ == "__main__":
    unittest.main()