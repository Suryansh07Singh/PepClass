'''marks = int(input("Enter marks: "))
grade = "Distinction" if marks >= 75 else "First Class" if marks >= 60 else "Pass" if marks >= 40 else "Fail"
print("Final Grade:", grade)

l1=[10, 20, 30, 40, 50]
len(l1)
print(id(l1))
l1[1]=9
print(l1)
print(id(l1))

l1=[10, 20, 30, 40, 50]
l1.append(60)
#help(l1.append)
l1.insert(2, 25)
print(l1)
l1.extend("Hii")
print(l1)'''

l1 = [3, 2, 2, 1, 3, 2]
indexes = []
for i in range(len(l1)):
    if l1[i] == 2:
        indexes.append(i)
print(indexes)


