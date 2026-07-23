# for loop in range

# a = "nature"
# for i in range(len(a)):
#     print(a[i])

# questions on loops 
#1 print hello wolrd 10 time
# n = int (input("please tell many time you want to print:-"))

# for i in range(n):
#     print(f"{i}: hello world")

# 2 print number from 1 to n

# n = int (input("Till where you want your number :-"))

# for i in range(1,n+1):
#     print(i)

# 3 print number from n to 1

# n = int (input("Till where you want your number :-"))

# for i in range(n,0,-1):
#     print(i)

#4 sum of natural number from 1 to n 

# n = int(input("till where you want to sum :-"))

# s = 0
# for i in range(1,n+1):
#     s =s+i
# print(f"your sum{s}")  

#5 factorial of number 
# n = int(input("which number factorial you want  :-"))

# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"your factorial is {fact}")  

# 6 sum of even odd number in range 
# n = int(input("tell you range"))

# even_sum =0
# odd_sum =0
# for i in range(1,n+1):
#     if i%2 ==0:
#         even_sum += i
#     else:
#         odd_sum += i
# print(f"hello your even sum is{even_sum} and your odd sum is {odd_sum}")            

# 7 print all factor of number
# n = int(input("What number factor i want to find:-"))

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# 8 sum of factors 
# n = int(input("What number factor sum you want:-"))
# sum = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         sum = sum + i
#         print(f"your factor sum is {sum}")

#9 
# a = int(input("tell your Value :-"))
# b = int(input("tell your exponent :-"))
# power = a
# for i in range(b-1):
#     power = power * a
# print(f"After power your answer is {power}")    

# 10 
n = int(input("give your number prime check:-"))
count = 0

for i in range(1,n+1):
    if n % i == 0:
        count = count + 1 
if count ==1:
    print("your number is unity number")
elif count ==2:
    print("your number is prime")
else :
    print("your number is composite")        