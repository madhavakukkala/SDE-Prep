class Sorting():

    def selection_sort(self,arr,n):
        for i in range(n-1):
            mini = i
            for j in range(i,n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i] , arr[mini]= arr[mini], arr[i]
        print(arr)

     
    def Bubblesort(self,arr,n):
        for i in range(n-1,0,-1):
            didswap = 0
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    didswap = 1
            if didswap == 0:
                break
        print(arr)


    def Insertionsort(self,arr,n):
        for i in range(n):
            j=1
            while j>0 and arr[j-1] > arr[j]:
                    arr[j-1],arr[j] = arr[j],arr[j-1]
        print(arr)

        for i in range(n):
            j = i
            while j>0 and arr[j-1]>arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -=1
        print(arr)


    def Mergesort():
        pass
        
        





if __name__ == '__main__':
    algo = Sorting()

    arr = [54,3,2,56,7,5,8,36,89,98,65,43,32,67,87]
    n = len(arr)

    algo.selection_sort(arr,n)
    # algo.Bubblesort(arr,n)
    # algo.Insertionsort(arr,n)

