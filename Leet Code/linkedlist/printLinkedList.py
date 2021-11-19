class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = 1
    
    def printList(self):
            
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':
    llist = LinkedList()
    
    llist.head = Node(1)
    # print(llist.head.next)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    # print(second.data)
    
    llist.printList()
    









class Node(object):
    
    def __init__(self,val= None):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        
        if(index >= self.size or index <0):
            return -1
        
        if(self.head is None):
            return -1
        
        curr = self.head
        
        p = curr
        
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return None
    

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val)
        
        else:
            curr = self.head

            while(curr.next):
                curr = curr.next

            new_node = Node(val)
            curr.next = new_node
        self.size += 1
        return None
    
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if(index > self.size or index <0):
            return -1
        
        if(index == 0):
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next

            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        
        if(index >= self.size or index <0):
            return -1
        
        if(index == 0):
            self.head = self.head.next
        
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next

            curr.next = curr.next.next
        self.size -= 1
        print(self.size)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
