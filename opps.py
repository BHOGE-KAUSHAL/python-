# class in python - 

# class Factory:
#     a=12 # attribute
#     def hello ():
#         print("how are you")

#     print("i am getting initialized")
# print(Factory.a)        
# Factory.hello()

# object -

# class Factory:
#     a= 'hello i am an attribute'
#     def hello (s):
#         print("hello i am method")

# obj=Factory()
# obj2 = Factory()
# print(obj.a)
# obj2.hello()

# constructor - is method that run automatically whenever we call class
# and constructor will target the location of the object 

# class Factory:
#     def __init__(self , material ,zips, pockets):
#         self.material = material
#         self.zips = zips 
#         self.pockets = pockets 
#     def showdetails(self):
#         print(self.material,self.pockets,self.zips)

# reebok = Factory("Leather",3,3)
# campus = Factory("Nylon",2,2)

# reebok.showdetails()

#--------------------

# class Animal:
#     gender = "male" # class Attribute

#     def __init__(self,name,age):
#         self.name = name # instance attribute
#         self.age = age # instance attribute

#     def info(self):    # intance Method
#         print("this is a method")

#     @classmethod
#     def clmethod(cls):  # class method
#         print(f"{cls.gender} is your gender")

#     @staticmethod
#     def hello():
#         print("hello I am a static method") 

# obj = Animal("Lion",12)
# obj.info()
# obj.clmethod()
# obj.hello()           


# make student registration system ask for name ,age, number ,blood group ,register 3 students

# class Registration:
#     def __init__(self,name,age , number ,blood):
#         self.age = age
#         self.name = name
#         self.number = number
#         self.blood = blood

#     def info(self):
#         print(f"hello your name is {self.name} \n your age is {self.age} \n your number is {self.number} \n your blood group is {self.blood} ")   
          
# student1 = Registration("Akarsh",22,9988776655,'A+')
# student2 = Registration("Ankur",23,9988776655,'B+')
# student3 = Registration("harsh",24,9988776655,'O-')

# student2.info()


