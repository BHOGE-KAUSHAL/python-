# SET
# s ={10,"hello",(1,2,3),12.5,True,print()}
#you can only store hashables value inside set

#unordered Nature
# s = {10,40,50,20,60,80}
# print(s)

#you cannot have duplicate value
# s={10,10,10,20,20,20,30,30}
# print(s)

#traversing on the set 
# s={12,13,24,56,12,12,78}
# for i in s:
#     print(i)

# set method -
# s={10,30,50,70}
# s.add(20)
# s.copy()
# print(s)

#differece in set method
# s1={12,20,30,40}
# s2={50,60,70,80}
# print(s2 - s1)

# discard

# s1={12,20,30,40}
# s2={50,60,70,80}
# s1.discard(20)
# print(s1)

# intersection
# s1={12,20,30,40}
# s2={50,60,70,80}
# print(s1 & s2)

#pop 
# s2={50,60,70,80}
# s2.pop()
# print(s2)

#union 
s1={12,20,30,40}
s2={50,60,70,80}
print(s1 | s2)