#1 sum ansd average of list

# a =[12,20,30, 40, 50]
# sum = 0
# for i in a:
#     sum =sum + i


# print(f"sum of your list number is{sum}")
# print(f"avg of your list number is{sum/len(a)}")

# 2 Maximun element with index

# a = [1,45,23,89,45,67,98,83 ,65]
# max =a[0]
# index =0

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"your maximum element is {max} at index{index}")        

#3 second greatest element

# a = [1,45,23,89,45,67,98,93,83 ,65]
# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i

# print(f"max {max} at index {index} and max 2 is {max2} at {index2}")             

# 4 check if list is sorted(increasing)
# a = [12,13,16,17,23,25,45,50,70,80,90]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")
     

# 5 left roatation by 1
# a =[10,20,30,40,50]
# for i in range(len(a)-1):
#     a[i],a[i-1] = a[i-1] ,a[i]
# print(a)  
# #  right  
# a =[10,20,30,40,50]
# for i in range(len(a)-1,0,-1):
#     a[i],a[i-1] = a[i-1] ,a[i]
# print(a)  

# 6 left roatation by 1 in k time 
# k =int(input("how many times you want to rotate"))
# a =[10,20,30,40,50]
# for i in range(k):
#     for i in range(len(a)-1):
#         a[i],a[i-1] = a[i-1] ,a[i]
# print(a)

# 7 Reverse the list (using swap element)
# a =[12,20,30,40,50]
# b = len(a)-1 
# for i in range(len(a)//2):
#     a[i],a[b] = a[b] ,a[i]
#     b = b -1
# print(a)    

# searching and sorting question
# 1  linear search
 
# a=[23,54,123,43,76,6,10,24,45]
# search = 76
# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element found at index {i}")
#         break
# else:
#     print("sorry no such element exist")    

#2 binary search - use divide and conqure method
# a =[12,14,16,23,25,43,34,37,57,68,70]
# search = 43
# start = 0
# last = len(a)-1
# mid =(start + last)// 2
# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a [mid] < search:
#         start = mid + 1
#         mid = (start + last) // 2
#     elif a[mid] > search:
#         last = mid -1
#         mid = (start + last) // 2
# else:
#     print("sorry no such element exist ")               

# bubble sort
# a =[12,14,16,23,25,143,234,337,57,68,70]
# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a [i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)            

# selection sort 
a =[12,14,16,23,25,143,234,337,57,68,70]

for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k] < a[min]:
            min = k
    a[i],a[min] = a[min],a[i]

print(a)            