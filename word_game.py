inpt=['a','b','c','d','e','f','g','h','i','j','k']
index=0
pointer_count=1
while len(inpt)!=1:
    if pointer_count%4==0 or pointer_count%10==4:
        inpt.remove(inpt[index])
        index+=1
    if index >=len(inpt)-1:
        index=0
    else:
        index+=1
    pointer_count+=1
print(inpt)
