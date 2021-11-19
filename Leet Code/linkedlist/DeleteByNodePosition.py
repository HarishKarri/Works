class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,new_data):
        new_node = Node(new_data)
        
        if(self.head is None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self,previous_val,new_data):
        new_node = Node(new_data)
        if(previous_val is None):
            return "Needs to be valid Value"
        
        flag = False
        last = self.head
        while(last):
            if(last.data == previous_val):
                break
            else:
                last = last.next
        if(last is None):
            return "No Value found"
        new_node.next = last.next
        last.next = new_node
    
    def deleteNode(self,pos):
        
        temp = self.head
        c = 0
        if(temp is not None):
            if(pos == 0):
                self.head = temp.next
                temp = None
                return 
        
        while(temp):
            
            if(c ==  pos):
                break;
            c += 1
            prev = temp
            temp = temp.next 
        
        if(temp == None):
            return "Not Found"
        
        prev.next = temp.next
        temp = None
        
    def printList(self):
            
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':
    llist = LinkedList()
    
    llist.append(3)
    llist.append(4)
    llist.push(1)
    llist.insertAfter(1,2)
    llist.insertAfter(10,20)
    llist.deleteNode(3) #3 is node position
    llist.deleteNode(4)
    llist.deleteNode(1)
        
    llist.printList()