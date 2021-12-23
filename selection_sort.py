class Solution: 
    def select(self, arr, i):
        # code here 
        min_index = i
        # print(min_index)
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr,n):
        #code here
        starting = 0
        for i in range(n):
            minimum = self.select(arr, starting)
            arr[minimum], arr[starting] = arr[starting] , arr[minimum]                  # they have exchanged place.
            starting += 1
        return arr