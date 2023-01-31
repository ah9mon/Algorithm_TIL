class Stack:
   
    def __init__(self):
        self.name = []
   

    def empty(self):
        if self.name == [] :
            return True
        else: 
            return False

    def top(self): 
        if self.name == [] :
            return None
        else:
            return self.name[-1]
        
    def pop(self):
        if self.name == [] :
            return None
        else:
           return self.name.pop()

    def push(self,x):
        self.name.append(x)

    def __repr__(self):
        return f'{self.name}'


a = Stack()
a.push(1)
a.push(2)
print(a.__repr__())
print(a.pop())
print(a.top())
print(a.pop())
print(a.top())
print(a.empty())


