maxinput=int(input("enter max limit"))
odd=[]
for i in range(1,maxinput+1):
    if i%2!=0:
        odd.append(i)
print(odd)
