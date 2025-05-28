class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description

class Queue:
    def __init__(self):
        self.tickets_list = []

    def enqueue(self, item):
        self.tickets_list.append(item)

    def dequeue(self):
        for item in self.tickets_list:
            self.tickets_list.remove(item)

    def peek(self):
        finalList = []
        
        for item in self.tickets_list:
            finalList.append(item)
        
        return finalList
    
class Stack:
    def __init__(self):
        self.tickets_list = []

    def push(self, item):
        self.tickets_list.append(item)

    def pop(self):
        for item in self.tickets_list:
            self.tickets_list.remove(item)

    def peek(self):
        finalList = []
        
        for item in self.tickets_list:
            finalList.append(item)
        
        return finalList