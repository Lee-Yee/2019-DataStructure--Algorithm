from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def key1(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        key1 = int(h.hexdigest(),16)
        return key1
        
    def add(self, key):
        key1 = self.key1(key)
        index = key1 % self.capacity
        if self.data[index] != None:
            head = self.data[index]            
            while head.next == None:               
                head.next = ListNode(key1)
            head = head.next 
        else:
            self.data[index] = ListNode(key1)    
  
    def contains(self, key):
        key1 = self.key1(key)
        index = key1 % self.capacity
        h=self.data[index]
        while h != None:
            if h.val != key1:
                h = h.next
            else:
                h = h.next
                return True
        else:
            return False
        
    def remove(self, key):
        key1 = self.key1(key)
        index = key1 % self.capacity                         
        if self.data[index].val != key1:
            while self.data[index]:
                if self.data[index].next == key1:
                    self.data[index].next = self.data[index].next.next
                    return
                self.data[index] = self.data[index].next
            return False
        elif self.data[index].val == key1:
            if self.data[index].next != True:
                self.data[index] = None
            else:
                self.data[index] = self.data[index].next
                self.data[index] = None
        else:          
            return False
