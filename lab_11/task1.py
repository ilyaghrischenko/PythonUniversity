class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.items:
            raise QueueError("Queue is empty")
        return self.items.pop(0)

    def isempty(self):
        return len(self.items) == 0


class SuperQueue(Queue):
    def isempty(self):
        return len(self.items) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
