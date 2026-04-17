
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.queue = [] # queue [].pop(0) first in frist out , we are gonna reaplcy by new one
        self.store = defaultdict(int)
    def get(self, key: int) -> int:
        if key in self.store:
            self.queue.remove(key)
            self.queue.append(key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else: 
            if len(self.queue) < self.size:
                self.store[key] = value
                self.queue.append(key)
            else:
                del_key = self.queue.pop(0)
                del self.store[del_key]
                self.store[key] = value
                self.queue.append(key)

        
