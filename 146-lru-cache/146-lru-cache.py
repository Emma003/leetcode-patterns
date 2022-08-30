class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        
        #maps key to linked list nodes
        self.cache = {}
        
        #doubly linked list: front = mru, back = lru 
        self.front = self.back = Node(0)
        self.front.next, self.back.prev = self.back,self.front

    def get(self, key: int) -> int:
        #retrieve value
        if key in self.cache:
            res = self.cache[key]
            
            #update mru
            self.remove(res)
            self.addFront(res)
            
            #return result
            return res.val
        
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        #if key exists
        if key in self.cache:
            res = self.cache[key]
            
            #remove from cache
            self.remove(res)
            
            #update value
            res.val = value
            
            #add back to front of cache
            self.addFront(res)
        
        
        #if key doesnt exist
        else: 
            #add k-v pair
            self.cache[key] = Node(key, value)
            
            #add to front of cache
            self.addFront(self.cache[key])
            
        #if len(cache) > capacity
        if len(self.cache) > self.cap:
            
            #retrieve the LRU node
            lru = self.back.prev
            
            #remove it from list
            self.remove(lru)
            
            #delete from cache
            del self.cache[lru.key]
        
    def addFront(self,node):
        node.next, node.prev = self.front.next, self.front
        self.front.next = node
        node.next.prev = node
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)