# while loop - work on condition and
#loop will stop when the condition became false
# a = 0
# while a < 10:
#     print(a)
#     a = a + 1 

 
# Break -break the loop
# continue - stop an particular iteration and continue the loop
#else - if break keyword is encounterd then else block will execute 

# for i in range(1,6):
#     if i == 8:
#         break
#     print(i)
# else:
#     print("no break executed") 

# question 1 
#print each digit in reverse order

# a = 145 
# while a > 0:
#     print(a % 10)
#     a = a // 10

#question 2
# sum of all digits - 

# a = int(input("please tell your number"))
# s = 0
# while a > 0:
#      s = s + a %10
#      a = a // 10
# print(f"your digit sum is {s}") 

#3 reverse the order

# a = int(input("please tell your number"))
# rev = 0 
# while a>0:
#     rev = rev * 10 + a%10
#     a = a // 10
# print(f"your number reverse is {rev}")    

# 4 
a = int(input("please tell your number"))
copy = a
rev = 0 
while a>0:

    rev = rev * 10 + a%10
    a = a // 10
if rev == copy:
    print("yes your number are pallindrome")
else:
    print("sorry your number is not pallindrome")        