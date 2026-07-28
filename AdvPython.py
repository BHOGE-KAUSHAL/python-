# Advance python 

# square = lambda a: print(a**2)
# square(12)
# #
# add = lambda x ,y:x+y
# print(add(12,12))

#map ,filter,zip
# map - purpose apply function to every item of an iterable and return a new iterable 
#  syntax = map(function ,iterable)

# def square(x):
#     return x**2
# a = [1,2,3,4]
# l = map(square,a)
# print(list(l))

#Filter:-
# purpose - filter items from an iterable boased on a condition
#syntax - filter(function,iterable)

# a = [1,2,3,4,5,6]
# l = filter(lambda x :x%2 == 0 ,a)
# print(list(l))

#zip
#purpose : combine muiltple iterables into pairs of elements.
# syntax =zip(iterable1,iterable2,...)
# name=["Akarsh", "Rahul","Priya"]
# ages = [24,22,23]

# comb = zip(name,ages)
# print(dict(list(comb)))


# 
a=[1,2,3,4,5,6,7,8,9]
l={i:i**2 for i in a if i %2 == 0}
print(l)
