number=[1,3,4,5,7,8,9,11,20]
odd=[]
even=[]

for i in range(0,len(number)):
    if number[i]%2 == 0:
        even.append(number[i])
    else :
        odd.append(number[i])

print(odd)
print(even)