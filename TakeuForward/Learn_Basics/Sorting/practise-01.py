# def selectionsort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         mini = i
#         for j in range(i,n):
#             if arr[j]<arr[mini]:
#                 mini = j
#         arr[i], arr[mini] = arr[mini], arr[i]
#     return arr


# def mergesort(arr):
#     n = len(arr)
#     if n<=1:
#         return arr
#     mid = n//2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = mergesort(left)
#     right = mergesort(right)

#     return merge(left, right)
# def merge(left, right):
#     temp = []
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i] < right[j]:
#             temp.append(left[i])
#             i+=1
#         else:
#             temp.append(right[j])
#             j+=1
        
#     temp.extend(left[i:])
#     temp.extend(right[j:])
    
#     return temp


# def quicksort(arr,low,high):
#     if low<high:
#         pivot_index = partition(arr, low , high)
#         quicksort(arr, low , pivot_index-1)
#         quicksort(arr, pivot_index+1 , high)
        
#     return arr
# def partition(arr, low , high):
#     pivot = arr[high]
#     i = low-1
#     for j in range(low , high):
#         if arr[j]<pivot:
#             i+=1
#             arr[i],arr[j] = arr[j] , arr[i]
#     arr[i+1],arr[high] = arr[high], arr[i+1]
#     return i+1

# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n-1,0,-1):
#         for j in range(i):
#             if arr[j]>arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr

# def insertionsort(arr):
#     n = len(arr)
#     for i in range(0,n):
#         j=i
#         while j>0 and arr[j-1]>arr[j]:
#             arr[j-1], arr[j] = arr[j] , arr[j-1]    
#             j-=1
#     return arr



    



# arr = [4, 2, 7, 2, 9, 4, 1]

# # temp = arr
# # print(selectionsort(temp))
# # temp = arr
# # print(mergesort(temp))
# # temp = arr
# # print(quicksort(temp,0,(len(temp)-1)))
# # temp = arr
# # print(bubblesort(temp))
# # temp = arr
# print(insertionsort(arr))



def selectionsort(arr,n):
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j]<arr[mini]:
                mini = j
            arr[i],arr[mini]=arr[mini],arr[i]
    return arr


def bubblesort(arr,n):
    for i in range(n-1,0,-1):
        didswap = 0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                didswap = 1
        if didswap==0:
            break
    return arr


def insertionsort(arr,n):
    for i in range(0,n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1] 
            j-=1
    return arr




arr = [4, 2, 7, 2, 9, 4, 1]
n = len(arr)
# print(selectionsort(arr,n))
print(insertionsort(arr,n))
# print(bubblesort(arr,n))




