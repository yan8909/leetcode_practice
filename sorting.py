def bubbleSort(arr):
    endPoint = len(arr) - 1
    while endPoint > 1:
        endPoint -= 1
        for i in range(endPoint):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        currentData = arr[i]
        index = i - 1
        while currentData <= arr[index] and index >= 0:
            arr[index+1] = arr[index]
            index -= 1
        arr[index+1] = currentData


def quickSort(arr, front, end):
    if front < end:
        pivot = partition(arr, front, end)
        quickSort(arr, front, pivot-1)
        quickSort(arr, pivot, end)

def partition(arr, front, end):
    pivot = arr[end]
    i = front - 1
    for j in range(front, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]

    return i

