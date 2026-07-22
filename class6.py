age = int(input("please tell your age -"))

if age >= 18:
    print('hello you can vote')

else:
    print("sorry you can vote ")

#ternary operator 
print("vote") if age >= 18 else print("not vote")


# ELIF statment 
money = int(input('please give me 10 ,20,30 or above  '))
if money == 10:
    print("I Will Have a choco bar ")

elif money == 20:
     print("I Will Have a mango dolly ")

elif money == 30:
     print("I Will Have a cone ")

else:
    print("i will Have full course meal")     


