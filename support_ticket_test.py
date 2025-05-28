import unittest
from support_ticket import *

class TestBrowserHistory(unittest.TestCase):
    def test_ticket_enqueue(self):
        ticket1 = Ticket(1, "Test_ticket")
        queue1 = Queue()
        queue1.enqueue(ticket1.issue_description)
        self.assertEqual(queue1.tickets_list[-1], "Test_ticket")

    def test_ticket_dequeue(self):
        ticket1 = Ticket(1, "Test_ticket")
        queue1 = Queue()
        queue1.enqueue(ticket1.issue_description)
        queue1.dequeue()
        listAfterDequeue = []
        self.assertEqual(queue1.tickets_list, listAfterDequeue)

    def test_ticket_queue_peek(self):
        ticket1 = Ticket(1, "Test_ticket")
        queue1 = Queue()
        queue1.enqueue(ticket1.issue_description)
        anotherList = ["Test_ticket"]
        self.assertEqual(queue1.peek(), anotherList)

    def test_ticket_push(self):
        ticket1 = Ticket(1, "Test_ticket")
        stack1 = Stack()
        stack1.push(ticket1.issue_description)
        self.assertEqual(stack1.tickets_list[-1], "Test_ticket")

    def test_ticket_pop(self):
        ticket1 = Ticket(1, "Test_ticket")
        stack1 = Stack()
        stack1.push(ticket1.issue_description)
        listAfterPop = ["Test_ticket"]
        self.assertEqual(stack1.tickets_list, listAfterPop)

    def test_ticket_stack_peek(self):
        ticket1 = Ticket(1, "Test_ticket")
        stack1 = Stack()
        stack1.push(ticket1.issue_description)
        anotherList = ["Test_ticket"]
        self.assertEqual(stack1.peek(), anotherList)

if __name__ == "__main__":
    unittest.main()