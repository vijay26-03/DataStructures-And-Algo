coins=list(map(int,input().split()))
target=int(input())
sum=0
comb=[]
while(sum<target):
    if(max(coins)+sum<=target):
        sum+=max(coins)
        comb.append(max(coins))
    if(max(coins)+sum>target):
        coins.remove(max(coins))
print(comb)