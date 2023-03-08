from ting_file_management.abstract_queue import AbstractQueue


# task 1 - thiago guarino
class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if index not in range(0, len(self.queue)):
            raise IndexError
        return self.queue[index]
