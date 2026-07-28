# inheritance 
class Animal: # parent class ,super class
    def __init__(self,name,age):
        self.name = name    # instance attribute
        self.age = age    # instance attribute

    def info(self):    # intance Method
        print(f"your name is {self.name} and your age is {self.age}")

class Human(Animal):
    def __init__(self,name,age,number ,group):
        super().__init__(name,age)
        self.number = number
        self.group = group
class Robot (Human):
    def __init__(self, name, age, number, group):
        super().__init__(name, age, number, group)        

obj = Animal("Lion",12)
obj2 = Human("kaushal",24,1234567891,'B+')
obj2.info()            

# encapsulation 
# means bundling data and method into one unit(class)
#controlling the access of modifier 
#Access modifier - public , private,protected

class Animal:
    __name = "Lion"

    def speak(self):
        print("hello i will roar")

class Human(Animal):
    def say(self):
        print(f"hello my name is {super().__name}")

obj = Human()
obj.say()
                