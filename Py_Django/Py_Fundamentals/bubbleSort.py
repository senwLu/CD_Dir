def bubbleSort(arr):
    count = len(arr)
    while count > 0:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # take value at array i and i+1 and swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
        count -= 1
        print(arr)
    return arr


# print(bubbleSort([4, 8, 1, 5, 2, 7, 3, 6]))
# bubbleSort([4, 8, 1, 5, 2, 7, 3, 6])
