#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None


# In[2]:


def push(self, val):
    new_node = Node(val)
    
#     no node currently
    if self.head is None:
        self.head = new_node
        return 
    
#     otherwise reach the end and then insert
    last = self.head
    while last.next is not None:
        last = last.next
        
    last.next = new_node
    
LinkedList.push = push


# In[3]:


def pop(self):
    if self.head is None:
        raise Exception("Cannot pop. No value.")
        
#     case where there is only one node
    if self.head.next is None:
        val = self.head.val
        self.head = None #automatic garbage collection
        return val
    
#     case where there is 2 or more nodes
#     reach the previous to last node
    temp = self.head
    while temp.next is not None:
        prev = temp
        temp = temp.next
        
    val = temp.val
    prev.next = None
    return val 

LinkedList.pop = pop    


# In[4]:


def __str__(self):
    ret_str = '['
    temp = self.head
    
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next
        
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    
    return ret_str

LinkedList.__str__ = __str__


# In[5]:


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)


print(l)
print("Pop: " , l.pop())
print("Pop: " , l.pop())
print("Pop: " , l.pop())
print(l)


# In[6]:


def insert(self, index, val):
    new_node = Node(val)
    
    #     insertion at node 0 is defferent
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    #     for other indices
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
        
    prev.next = new_node
    new_node.next = temp
    
LinkedList.insert = insert


# In[7]:


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)


print(l)
print("Pop: " , l.pop())
print("Pop: " , l.pop())
print("Pop: " , l.pop())
print(l)

l.insert(0, 10)
l.insert(5, 19)
print(l)


# In[10]:


def remove(self, val):
    temp = self.head
    
#     check first node
    if temp is not None:
        if temp.val == val:
            self.head = temp.next
            temp = None
            return
        
#         lets move towards next nodes
# temps holds the value that will be deleted

    while temp is not None:
        if temp.val == val:
            break
            
        prev = temp
        temp = temp.next
        
    if temp is None:
        return
    
    prev.next = temp.next # just lose the reference to delete node
    
LinkedList.remove = remove


# In[11]:


def get(self, index):
    
    if index == 0:
        val = self.head.val
        return val
    
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        temp = temp.next
        counter += 1
        
    val = temp.val
    return val

LinkedList.get = get        


# In[15]:


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)

print(l)

l.get(0)


# In[ ]:




