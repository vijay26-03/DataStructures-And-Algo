from operator import index


coins=list(map(int,input().split()))
target=int(input())
comb=[]
while(target>0):
    if(max(coins)<=target):
        comb.append(max(coins))
        target-=max(coins)
    if(max(coins)>target):
        coins.remove(max(coins))
print(comb)







