import gc
class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):   #at end
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node 
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node
        new_node.prev = last
    
    def push(self,data): #at first
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            
            self.head = new_node
            return 
    
    def insertAfter(self,afterValue,data):
        new_node = Node(data)
        current = self.head
        while(current):
            if(current.data == afterValue):
                break;
            current = current.next
        
        if current is None:
            return "Not Found"
        
        
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        
        if new_node.next is not None:
            new_node.next.prev = new_node
        return 
        
    
    def insertBefore(self,beforeValue,data):
        new_node = Node(data)
        current = self.head
        while(current):
            if(current.data == beforeValue):
                break;
            current = current.next
        
        if current is None:
            return "Not Found"
        
        new_node.prev = current.prev
        current.prev = new_node
        new_node.next = current
        
        if(new_node.prev is None):
            self.head = new_node
        else:
            new_node.prev.next = new_node
        return 
    
    def printNode(self):
        n = self.head
        # print(n.data)
        while(n):
            print(n.data)
            n = n.next
        
    def deleteNode(self,data):
        
        current = self.head
        
        if(current.data == data):
            self.head = current.next
            gc.collect()
            return
        
        while(current):
            if(current.data == data):
                break;
            
            current = current.next
        
        if(current.next is None):
            current.prev.next = current.next
            gc.collect()
            return
        
        current.prev.next = current.next
        current.next.prev = current.prev
        gc.collect()
        return
    
    def reverse(self):
        temp = None
        current = self.head
 
        # Swap next and prev for all nodes of
        # doubly linked list
        while(current):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # print(current.data)
            current = current.prev
        
        # print(temp.data)
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
            # print(self.head.data)
            return

if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.append(6)
    llist.append(7)
    llist.push(5)
    llist.push(4)
    llist.insertAfter(7,8)
    llist.insertAfter(6,10)
    llist.insertBefore(6,11)
    llist.insertBefore(5,4)
    llist.insertBefore(6,11)
    llist.insertBefore(4,3)
    
    llist.printNode()
    
    print("FFF")
    
    llist.deleteNode(3)
    llist.deleteNode(8)
    llist.deleteNode(11)
    llist.deleteNode(4)
    llist.deleteNode(11)
    llist.printNode()
    print("reverse")
    llist.reverse()
    
    llist.printNode()
    