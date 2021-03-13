def handle(arrayA,arrayB):
    res=[]
    i=0
    j=0
    while(i<arrayA.__len__() and j<arrayB.__len__()):
        if arrayA[i]>arrayB[j]:j+=1
        elif arrayA[i]<arrayB[j]:i+=1
        else:
            res.append(arrayA[i])
            i+=1
            j+=1
    return res
arrayA=[1, 1, 2, 3, 5, 8, 15, 21, 34, 56, 86]
arrayB=[0,8,9,11,15]
print(handle(arrayA,arrayB))
