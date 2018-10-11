def insertionSort(arr):
    # starting from first two array values
    # compare which one is smaller
    # move smaller value and compare it back towards beginning of array
    # stop moving back insertion value and insert when insertion value is larger than compared value
    # repeat

    # count = 0
    # for i in range(count, len(arr)-1):
    #     # if value after current value is smaller
    #     if arr[i] > arr[i+1]:

    #         # get where arr[i+1] is in the array
    #         start = arr.index(arr[i+1])

            # loop back towards beginning of array
            # for a in range(start, 0, -1):

            # # if value is smaller keep swapping back towards begining of array
            # # stop swapping value back when value is larger to the next compared value
            # if arr[a] < arr[a-1]:
            #     arr[a], arr[a-1] = arr[a-1], arr[a]

            ########################################################################

    # loop up the arr
    for index in range(1, len(arr)):

        # grab value at index and set to currentValue
        currentValue = arr[index]

        # continue to loop if index is greater than 0
        # and if currentValue is smaller than the value below it
        while index > 0 and currentValue < arr[index-1]:

            arr[index] = arr[index-1]
            index -= 1

        arr[index] = currentValue

    print(arr)


insertionSort([4, 8, 5, 2, 3, 1, 6, 9, 7])

# 4, 8, 5, 2
# 4, 8, 8, 2 => break out of loop => 4, 5, 8, 2
# 4, 5, 8, 2
# 4, 5, 8, 8
# 4, 5, 5, 8
# 4, 4, 5, 8 => break out of loop 2, 4, 5, 8
# 2, 4, 5, 8
