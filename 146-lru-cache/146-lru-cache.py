class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.front = self.back = Node()
        self.front.next, self.back.prev = self.back, self.front
        
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key]
            self.remove(res)
            self.addFront(res)
            return res.val
        
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            res = self.cache[key]
            self.remove(res)
            res.val = value
            self.addFront(res)
        else:
            
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.addFront(newNode)
            
            
        #remove lru
        if len(self.cache) > self.capacity:
            lru = self.back.prev
            lru.prev.next = self.back
            lru.next.prev = lru.prev
            
            del self.cache[lru.key]
            
    
    #helper functions
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def addFront(self,node):
        node.next = self.front.next
        node.prev = self.front
        self.front.next = node
        node.next.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)