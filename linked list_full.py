#!/usr/bin/env python
# coding: utf-8

# In[85]:


class Node :
    def __init__(self,data=None,next=None):
        self.data = data
        self.next= next 
        


# In[89]:


class linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head = node
        
        
    def print(self):
        if self.head is None:
            print("list is empty")
            return
        ret_str = ''
        temp = self.head   
        while temp is not None:
            ret_str += str(temp.data) + "-->"
            temp=temp.next
            
        return ret_str
        #print(ret_str)
#         ret_str = ret_str.rstrip(', ')
    
    
    def insert_at_ending(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        temp = self.head 
        while temp.next is not None:
            temp = temp.next
        
        temp.next = Node(data,None)
            
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_ending(data)
            
    def get_length(self):
        count=0
        temp=self.head 
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    
    def remove(self,index):
        if index <0 or index>=self.get_length():
            raise Exception("invalid index")
            
        if index ==0:
            self.head = self.head.next
            return
        count =0
        
        temp = self.head
        while temp is not None:
            if count == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count +=1
            
            
        
            


# In[90]:



ll = linkedlist()
# ll.insert_at_begining(5)
# ll.insert_at_begining(10)
# ll.insert_at_begining(15)
# ll.insert_at_begining(20)
# ll.insert_at_ending(30)
# ll.insert_at_ending(40)
# ll.print()

ll.insert_values(["ali","aamir","fazal","adnan"])
# ll.print()
# ll.get_length()
ll.remove(2)
ll.print()
            


# In[ ]:



    


# In[24]:





# In[ ]:





# In[ ]:





# In[ ]:




