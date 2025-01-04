def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = findSmallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr


print(selectionSort([90,109,11,83,105,54,60,13,56,111]))