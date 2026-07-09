def selectionsort(arr,n):
    for i in range(n-1):
        mini=i
        for j in range(i,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr

def bubblesort(arr,n):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def insertionsort(arr,n):
    for i in range(n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr

arr = [9,12,15,31,6,8,3,18,1]
n = len(arr)
# print(selectionsort(arr,n))
# print(bubblesort(arr,n))
print(insertionsort(arr,n))