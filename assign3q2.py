s1="How much wood would a woodchuck chuck if a Woodchuck could chuck wood to build a wooden house to woo his wife"
out=[]
s1=s1.split()
for i in s1:
    if len(i)>=4 and i.startswith(('w','W')):
        if i not in out:
            out.append(i)
print(out)