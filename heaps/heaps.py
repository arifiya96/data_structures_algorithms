import math

class check_heap:
    def max_heap(self, array):
        is_heap = True
        for i in range(1,len(array)):
            if array[i] >= array[int(math.floor((i-1)/2))]:
                is_heap = False
        print(is_heap)
    
    def min_heap(self, array):
        is_heap = True
        for i in range(1,len(array)):
            if array[i] <= array[int(math.floor((i-1)/2))]:
                is_heap = False
        print(is_heap)

class heap_operations:
    def max_heapify(self, array):
        for i in range(len(array)-1,0,-1):
            if array[i] > array[int(math.floor((i-1)/2))]:
                array[i], array[int(math.floor((i-1)/2))] = array[int(math.floor((i-1)/2))], array[i]
        print(array)

testing_array_max = [20,19,15,6,2,8]
testing_array_min = [2,6,10,17,21,11]
testing_array_unordered = [2,5,3,10,4,6,9]

"""Check if it is a heap"""
validate = check_heap()
validate.max_heap(testing_array_max)
validate.min_heap(testing_array_min)

"""Heap operations"""
functions = heap_operations()
functions.max_heapify(testing_array_unordered)

