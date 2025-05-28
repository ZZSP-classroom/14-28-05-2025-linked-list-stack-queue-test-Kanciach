class Queue:
    def __init__(self):
        self.items_list = []

    def enqueue(self, item):
        self.items_list.append(item)

    def dequeue(self):
        for item in self.items_list:
            self.items_list.remove(item)

    def peek(self):
        finalList = []
        
        for item in self.items_list:
            finalList.append(item)
        
        return finalList