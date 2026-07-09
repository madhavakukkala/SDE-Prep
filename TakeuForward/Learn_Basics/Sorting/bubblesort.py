'''
Bubble sort : 

13 , 46 , 24 , 52, 20, 9


by pushing the maximum  to the last by adjacent swaps 


'''


def Bubblesort(arr,n):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

        





arr = [54,3,2,56,7,5,8,36,89,98,65,43,32,67,87]
n = len(arr)

Bubblesort(arr,n)