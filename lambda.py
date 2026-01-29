#Used to define a function in single line without any name.
#Syntax: lambda arguments: expression

add=lambda a,b:a+b
print(add(14,15))

sq=lambda x:x**3
print(sq(9))


#map function map() applies a function to every item in an iterable (like a list, tuple, etc.) and returns the transformed result.
num=[1,2,3,4,5,6,7,8,9]
res=map(lambda x:x**2,num)
print(list(res))

#Which is better lambda or using loop or list comprehension?
#Using list comprehension is better than lambda as it is more readable and faster in execution.
#Example using list comprehension to get squares of numbers
squares=[x**2 for x in num]
print(squares)

#I want to add these two lists using loop.
l1=[3,2,2,1,3,2,5]
l2=[4,8,6,5,3,2,6]
l3=[]

if len(l1)>len(l2):
    l2.append(0)
elif len(l2)>len(l1):
    l1.append(0)
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)

#filter function
#The filter() function constructs an iterator from elements of an iterable for which a function returns true
#filter(function, iterable)
evens=filter(lambda x:x%2==0,num)
print(list(evens))

a=filter(lambda x:x-1,[1,2,3,4,5])
print(list(a))

#reduce function
#“Combine all elements step-by-step into one result.”
#This function is defined in "functools" module.

from functools import reduce
s1=["Hello","World","in","Python"]
res=reduce(lambda x,y:x+y,s1)
print(res)