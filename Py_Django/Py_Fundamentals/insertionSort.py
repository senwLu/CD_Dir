def insertionSort(arr):
    # starting from first two array values
    # compare which one is smaller
    # move smaller value and compare it back towards beginning of array
    # stop moving back insertion value and insert when insertion value is larger than compared value
    # repeat

    count = 0
    for i in range(count, len(arr)-1):
        # if value after current value is smaller
        if arr[i] > arr[i+1]:

            # get where arr[i+1] is in the array
            start = arr.index(arr[i+1])

            # loop back towards beginning of array
            # for a in range(start, 0, -1):

            # # if value is smaller keep swapping back towards begining of array
            # # stop swapping value back when value is larger to the next compared value
            # if arr[a] < arr[a-1]:
            #     arr[a], arr[a-1] = arr[a-1], arr[a]

            ########################################################################

            checker = arr[i+1]
            # print(checker)
            # break
            # keep looping back and insert only when value is larger than next compared value
            for a in range(start, -1, -1):
                if checker > arr[a]:
                    checker = arr[a]
                    break

            # print(checker)


insertionSort([4, 8, 5, 2, 3, 1, 6, 9, 7])
