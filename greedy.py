l=list(map(int,input().split()))
l.sort(reverse=True)
target=int(input())
possible_combination=[]
index=0
while(target>0):
    if target>=l[index]:
        target-=l[index]
        possible_combination.append(l[index])
    else:
        index+=1
print (possible_combination)