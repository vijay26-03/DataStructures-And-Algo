from itertools import combinations_with_replacement as cwr
l=list(map(int,input().split()))
target=int(input())
pos_comb=[]
for i in range(target+1):
    for j in cwr(l,i):
        if(sum(j) == target):
            pos_comb.append(list(j))
print(pos_comb)