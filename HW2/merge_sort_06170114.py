###### merge_sort_06170114.py

class Solution(object):
    def merge_sort(self,mylist):
        if len(mylist)>1:
            mid = len(mylist)//2
            l = mylist[:mid]
            r = mylist[mid:]
            self.merge_sort(l)
            self.merge_sort(r)
            i=0
            j=0
            k=0
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    mylist[k]=l[i]
                    i=i+1
                else:
                    mylist[k]=r[j]
                    j=j+1
                k=k+1

            while i < len(l):
                mylist[k]=l[i]
                i=i+1
                k=k+1

            while j < len(r):
                mylist[k]=r[j]
                j=j+1
                k=k+1


