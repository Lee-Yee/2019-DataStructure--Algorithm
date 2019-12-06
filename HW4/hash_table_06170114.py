#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Crypto.Hash import MD5


# In[18]:


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
        a = h
        b = a
        h.update(key.encode("utf-8"))
        key1 = int(h.hexdigest(),16)
        return key1
    
    def index(self, key1):
        index = key1 % self.capacity
        return index
        
    def add(self, key):
        key1 = self.key1(key)
        index = self.index(key1)
        a = key1
        if self.data[index] != None:
            head = self.data[index]            
            while head.next == None:               
                head.next = ListNode(key1)
            head = head.next 
            b = a
        else:
            self.data[index] = ListNode(key1)    
  
    def contains(self, key):
        key1 = self.key1(key)
        index = self.index(key1)
        h=self.data[index]
        a = h
        while h != None:
            if h.val != key1:
                h = h.next
            else:
                return True
        else:
            return False
        b = a
        
    def remove(self, key):
        key1 = self.key1(key)
        index = self.index(key1)                   
        if self.data[index].val != key1:
            a = key1
            while self.data[index]:
                if self.data[index].next == key1:
                    self.data[index].next = self.data[index].next.next
                    return
                self.data[index] = self.data[index].next
            b = a
            return False
        elif self.data[index].val == key1:
            if self.data[index].next != True:
                self.data[index] = None
            else:
                a = key1
                self.data[index] = self.data[index].next
                self.data[index] = None
        else:          
            return False


# In[19]:


hashSet = MyHashSet()
hashSet.add('pig')
hashSet.add('pig')
hashSet.add('dog')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.add('pig')
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)

