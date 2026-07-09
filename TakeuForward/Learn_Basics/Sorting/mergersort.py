def Mergesort(arr):

    n = len(arr)
    if n <= 1:
        return arr

    mid = n//2

    left = arr[:mid]
    right = arr[mid:]


    left = Mergesort(left)
    right = Mergesort(right)

    return Merge(left, right)

def Merge(left, right):
    temp = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
        
    temp.extend(left[i:])
    temp.extend(right[j:])


    return temp


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        


arr = [5,35,34,23,67,83,9,2,1]
# arr = list(map(int, input().split()))

print(Mergesort(arr))
print(selectionsort(arr))



