#!/usr/bin/env python
# coding: utf-8

# In[5]:


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[15]:


def insert(root, val): 
    if root.val > val: 
        if root.left is None: 
            root.left = TreeNode(val)
        else: 
            insert(root.left, val) 
    else: 
        if root is None: 
            root = TreeNode(val)
        elif root.right is None: 
            root.right = TreeNode(val)
        else: 
            insert(root.right, val) 


# In[16]:


def search(root, target):
    if target > root.val : 
        return search(root.right, target)
    if root.val > target:
        return search(root.left, target) 
    else:
        return root


# In[17]:


def modify(root, target, new_val):
    root = delete(root, target)  
    root = insert(root, new_val) 
    return root 


# In[18]:


def inorder(root):
    if root is None: 
        return     
    else:
        inorder(root.left) 
        print(root.val)
        inorder(root.right)


# In[19]:


def minval(root): 
    while root.left is not None:  
        root = root.left 
    return root  


# In[20]:


def maxval(root): 
    while root.right is not None:  
        root = root.right 
    return root


# In[21]:


def right_minval(root): 
    minval(root.rigt) 


# In[22]:


def left_maxval(root): 
    maxval(root.left)


# In[23]:


def delete(root, target): 
    if root == None:  
        return
    if root.val > target:  
        root.left = delete(root.left, target) 
    elif target > root.val:  
        root.right = delete(root.right, target) 
    else: 
        if root.right != None: 
            k = root.right 
            return k 
        if root.left != None: 
            k = root.left 
            return k 
            k = left_maxval(root)  
            root.target = k.target  
            root.left = delete(root.left, k.target) 
    return root


# In[24]:


a = TreeNode(9) 
insert(a,3) 
insert(a,0) 
insert(a,-6) 
insert(a,7.3) 
insert(a,-2) 
insert(a,3) 
insert(a,7) 
insert(a,6)

delete(a,7)

modify(a,-6,6)

inorder(a)


# In[3]:


#參考資料
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#https://www.geeksforgeeks.org/how-to-implement-decrease-key-or-change-key-in-binary-search-tree/


# In[ ]:




