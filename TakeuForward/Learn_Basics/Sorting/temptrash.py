def mergesort(arr,low,high):
    mid = (low+high) // 2

    if low>=high:
        return
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)

    merge(arr, low ,mid, high)


def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
    while left<=mid:
        temp.append(arr[left])
        left+=1
        
    while right<=high:
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]


arr=[6,87,2,6,987,8,3,2,8,0,3,2,6,89,975,4,32]
mergesort(arr,0,len(arr)-1)
print(*arr)


