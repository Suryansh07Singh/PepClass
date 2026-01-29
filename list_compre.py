nums=[1,2,3,4,5]
#squares=[x**2 for x in nums] list comprehension
'''squares=[]
for i in nums:
    squares.append(i**2)
print(squares)

for i in nums:
    if i%2==0:
        squares.append(i**3)
    else:
        squares.append(i**2)
print(squares)'''

l1=[i**3 if i%2==0 else i**2 for i in nums]
print(l1)