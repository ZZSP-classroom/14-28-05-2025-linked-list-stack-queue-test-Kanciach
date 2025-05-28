import unittest
from playlist_manager import *

class TestPlaylistManager(unittest.TestCase):
    def test_add_song(self):
        linkedList1 = LinkedList()
        linkedList1.insertAtBegin('a')
        linkedList1.insertAtEnd('b')
        self.assertEqual(linkedList1.head.data, 'a')

    def test_remove_song(self):
        linkedList1 = LinkedList()
        linkedList1.insertAtBegin('a')
        linkedList1.remove_first_node()
        self.assertIsNone(linkedList1.printLL())

    def test_get_next_song(self):
        linkedList1 = LinkedList()
        linkedList1.insertAtBegin('a')
        linkedList1.insertAtEnd('b')
        self.assertEqual(linkedList1.sizeOfLL(), 2)

if __name__ == "__main__":
    unittest.main()