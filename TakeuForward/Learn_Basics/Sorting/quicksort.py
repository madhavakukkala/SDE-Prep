def quicksort(arr, low, high):
    
    if low<high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low , pivot_index-1)
        quicksort(arr, pivot_index+1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j]< pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high]  = arr[high], arr[i+1]

    return i+1

def mergesort(arr):
    n = len(arr)

    if n<=1:
        return arr

    mid = n//2

    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return Merge(left, right)

def Merge(left, right):
    temp = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp





arr = [3,7,11,5,9,15]

print(arr)

sorted_arr = mergesort(arr)

print(sorted_arr)

print(arr)


# print(quicksort(arr, 0, (len(arr)-1)))
# print(mergesort(arr))

