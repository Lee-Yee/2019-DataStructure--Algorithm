##### heap_sort_06170114.py

class Solution(object):
    def swap(self,i,j):                    
        mylist[i],mylist[j]=mylist[j],mylist[i] 


    def heap_sort(self,mylist):     
        for i in range(len(mylist)//2,-1,-1):   
            self.heapify(len(mylist),i)   
        for i in range(len(mylist)-1,0,-1):   
            self.swap(i,0)   
            self.heapify(i,0) 
            
    def heapify(self,n,i):   
        c1=2*i+1  
        c2=2*i+2   
        pa=i   
        if c1<n and mylist[i]<mylist[c1]:   
            pa=c1  
        if c2<n and mylist[pa]<mylist[c2]:   
            pa=c2   
        if pa!=i:   
            self.swap(i,pa)   
            self.heapify(n,pa)   
