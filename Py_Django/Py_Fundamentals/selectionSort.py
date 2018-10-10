def selectionSort(arr):
    count = 0

    while count < len(arr):
        minNum = arr[count]

        for i in range(count, len(arr)):
            if minNum > arr[i]:
                minNum = arr[i]

        # get index of minNum
        a = arr.index(minNum)
        # swaps minNum with the value in the array at count
        arr[count], arr[a] = arr[a], arr[count]

        count += 1

    return arr


print(selectionSort([7, 4, 9, 1, 0, 8, 2, 5, 3, 6]))

# selectionSort([7, 4, 9, 1, 0, 8, 2, 5, 3, 6])
