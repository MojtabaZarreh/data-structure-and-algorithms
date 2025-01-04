# def QuickSort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr if i < pivot]
#         equal = [i for i in arr if i == pivot]
#         greater = [i for i in arr if i > pivot]
#         return QuickSort(less) + equal + QuickSort(greater)

# print(QuickSort([11,5,23,21,8,100]))

import random
def QuickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        print(f'pivot: {pivot}')
        
        less = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        greater = [i for i in arr if i > pivot]
        
        return QuickSort(less) + equal + QuickSort(greater)

print(QuickSort([11, 5, 23, 21, 8, 100]))
