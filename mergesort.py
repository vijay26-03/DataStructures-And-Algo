def sort(inpt):
    if (len(inpt)>1):
        mid=len(inpt)//2
        left=inpt[:mid]
        right=inpt[mid:]
        sort(left)
        sort(right)
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if (left[i]<right[j]):
                inpt[k]=left[i]
                i+=1
                k+=1
            else:
                inpt[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            inpt[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            inpt[k]=right[j]
            j+=1
            k+=1

inpt = list(map(int,input().split()))
sort(inpt)
print(inpt)