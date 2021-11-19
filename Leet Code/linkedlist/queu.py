class Queue:
    
    def __init__(self):
        self.queue = list()
        self.maxSize = 5
    def isFull(self):
        if(len(self.queue) == self.maxSize):
            return True
        return False
        
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        return False
    def addtoq(self,dataval):
        if(self.isFull()== False):
            self.queue.insert(0,dataval)
            return "Inserted"
        return "Queue Full"
          
    # Pop method to remove element
    def removefromq(self):
        if(self.isEmpty() == False):
            self.queue.pop()
            return "Deleted"
            
        return ("No elements in Queue!")
    def peek(self):
        return self.queue[0]
TheQueue = Queue()
print(TheQueue.addtoq("Mon"))
print(TheQueue.addtoq("Tue"))
print(TheQueue.addtoq("Wed"))
print(TheQueue.removefromq())
print(TheQueue.removefromq())
print(TheQueue.peek())