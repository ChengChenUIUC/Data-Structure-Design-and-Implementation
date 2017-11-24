class DLinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.post = None
        self.key = None
    
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = dict()
        self.c = capacity
        self.head = DLinkedNode(0)
        self.tail = DLinkedNode(0)
        self.head.post = self.tail
        self.tail.pre = self.head
        self.cnt = 0
    
    # always add node to head
    def addNode(self, node):
        node.post = self.head.post
        node.pre = self.head
        node.post.pre = node
        self.head.post = node
    
    # remove any node
    def removeNode(self, node):
        node.post.pre = node.pre
        node.pre.post = node.post
    
    # remove a node and add to head
    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)
        
    # pop the least used node:
    def popTail(self):
        realTail = self.tail.pre
        self.removeNode(realTail)
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash: return -1
        else:
            node = self.hash[key]
            self.moveToHead(node)
            return node.val
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            self.moveToHead(node)
        else:
            node = DLinkedNode(value)
            node.key = key
            self.hash[key] = node
            self.addNode(node)
            self.cnt += 1
            if self.cnt > self.c:
                k = self.tail.pre.key
                self.popTail()
                self.hash.pop(k)
                self.cnt -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)