from itertools import combinations_with_replacement as cwr

def check(pos_comb,target,index):
    if sum(pos_comb[index]) == target:
        print(pos_comb[index])
    else:
        check(pos_comb,target,index+1)

l=list(map(int,input().split()))
target=int(input())
pos_comb=[]
index=0
for i in range(target+1):
    for j in cwr(l,i):
        pos_comb.append(list(j))
check(pos_comb,target,index)