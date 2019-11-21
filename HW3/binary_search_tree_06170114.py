class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val): 
        if root.val > val: 
            if root.left is None: 
                root.left = TreeNode(val)
            else: 
                self.insert(root.left, val) 
        else: 
            if root is None: 
                root = TreeNode(val)
            elif root.right is None: 
                root.right = TreeNode(val)
            else: 
                self.insert(root.right, val) 
                
    def search(self, root, target):
        if target > root.val : 
            return self.search(root.right, target)
        if root.val > target:
            return self.search(root.left, target) 
        else:
            return root
        
    def modify(self, root, target, new_val):
        root = self.delete(root, target)  
        root = self.insert(root, new_val) 
        return root 
                    
    def inorder(self, root):
        if root is None: 
            return     
        else:
            self.inorder(root.left) 
            print(root.val)
            self.inorder(root.right)
            
    def minval(self, root): 
        while root .left is not None:  
            root  = root .left 
        return root  
    
    def maxval(self, root): 
        while root .right is not None:  
            root  = root .right 
        return root
    
    def right_minval(self, root): 
        self.minval(root.rigt) 
    
    def left_maxval(self, root): 
        self.maxval(root.left)

    def delete(self, root, target): 
        if root == None:  
            return
        if root.val > target:  
            root.left = self.delete(root.left, target) 
        elif target > root.val:  
            root.right = self.delete(root.right, target) 
        else: 
            if root.right != None: 
                k = root.right 
                return k 
            if root.left != None: 
                k = root.left 
                return k 
                k = self.left_maxval(root)  
                root.target = k.target  
                root.left = self.delete(root.left, k.target) 
        return root



#參考資料
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#https://www.geeksforgeeks.org/how-to-implement-decrease-key-or-change-key-in-binary-search-tree/
