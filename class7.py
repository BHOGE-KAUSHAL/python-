# question 1 - take two user input and determine which number are greater -or eqaual  
a = float(input("please tell your first number:"))
b = float(input("please tell your second number:"))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")    

# question 2,3  - accept gender input['m'] or ["f"] and print hello sir and hello mam
gen = input ("please tell your gender in character(m,f): -")

if gen == 'm' or gen =='M':
    print("hello sir how are you")
elif gen == 'f' or gen =='F':
    print("hello mam how are you")    
else:
    print("wrong input only provide m or f ")

# question 4 -check input wheather it even or odd using modulo
a = int(input("please tell me your number :-"))
if a % 2 == 0:
    print('your number is even')
else :
    print("your number is odd")    

# question 5 - 
name =input("please tell your name:-")
age =int(input("please tell your age:-")) 

if age >= 18 :
    print(f'hello {name} you can vote')
    