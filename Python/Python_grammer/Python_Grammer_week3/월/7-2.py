class Doggy:

    num_of_dogs = 0
    birth_of_dog = 0

    def  __init__(self,name,kind): 
        self.name = name 
        self.kind = kind
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dog += 1
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
        return f'num of dogs는 {Doggy.num_of_dogs}'


    def bart(self):
        return '왈왈'

    def get_status(self):
        return f'birth of dogs는 {Doggy.birth_of_dog} num of dogs는 {Doggy.num_of_dogs}'

my_dog = Doggy('왈왈이', '시츄')
print(my_dog.name) # 왈왈이
print(my_dog.kind) # 시츄
print(my_dog.bart()) # '왈왈'
print(my_dog.get_status()) # 
print(my_dog.__del__())

