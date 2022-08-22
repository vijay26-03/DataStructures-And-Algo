#refered geeks for geeks 
def partition(arr,low,high):
    i,j = low,high
    if low!=high and low<high:
        pivot_ele=arr[low]
        i=i+1
        while i<=j:
            if arr[j]<pivot_ele and arr[i]>pivot_ele:
                arr[j],arr[i] = arr[i],arr[j]
            if not arr[i]>pivot_ele:
                i+=1
            if not arr[j]<pivot_ele:
                j-=1
        arr[low],arr[j]=arr[j],arr[low]
        return j

def quick_sort(inpt,i,j):
    if i<j:
        pi=partition(inpt,i,j)
        quick_sort(inpt,i,pi-1)
        quick_sort(inpt,pi+1,j)


inpt = list(map(int,input().split()))
quick_sort(inpt,0,len(inpt)-1)
print(inpt)