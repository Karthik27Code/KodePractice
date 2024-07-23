import random


def quickSort(input : list):
    quickSortHelper(input, 0, len(input)-1)

""" This method chooses a pivot element and splits the list into 
    two parts. one part is less than the pivot element and the other
    part is greater than the pivot element."""
def partition(input: list, start: int, end: int) -> int:
    pivot = random.randrange(start, end, 1)
    input[end], input[pivot] = input[pivot], input[end]
    pivotElement = input[end]
    ind = start
    for j in range(start, end):
        if input[j] < pivotElement:
            input[ind], input[j] = input[j], input[ind]
            ind += 1

    input[ind], input[end] = input[end], input[ind]
    return ind


""" A helper method to perform the recursive quick sort operations
    partitioned list."""
def quickSortHelper(input: list, start:int, end: int):
    if start < end:
        pivot = partition(input, start, end)
        quickSortHelper(input, start, pivot-1)
        quickSortHelper(input, pivot+1, end)


inputArray = [1,5,3,2,8,7,6,4]
quickSort(inputArray)
print(inputArray)