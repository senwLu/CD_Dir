def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr


# print(biggieSize([-1, 3, 5, -5]))

def countPos(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr


# print(countPos([-1, 1, 0, 1]))

def sumTotal(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


# print(sumTotal([1, 2, 3, 4]))

def average(arr):
    avg = 0
    for i in range(len(arr)):
        avg += arr[i]
    return avg/len(arr)


# print(average([1, 2, 3, 4]))

def arrlength(arr):
    return len(arr)


# print(arrlength([1, 2, 3, 4]))

def findMin(arr):
    minNum = arr[0]
    if len(arr) == 0:
        return False
    else:
        for i in range(len(arr)):
            if minNum > arr[i]:
                minNum = arr[i]
    return minNum


# print(findMin([-1, -2, -3, 5]))

def findMax(arr):
    if len(arr) == 0:
        return False
    else:
        maxNum = arr[0]
        for i in range(len(arr)):
            if maxNum < arr[i]:
                maxNum = arr[i]
        return maxNum


# print(findMax([1, 2, 3]))

def ultiAnalyze(arr):
    s = sumTotal(arr)
    a = average(arr)
    m = findMin(arr)
    n = findMax(arr)
    l = arrlength(arr)

    return {
        'sumTotal': s,
        'average': a,
        'minimum': m,
        'maximum': n,
        'length': l
    }


# print(ultiAnalyze([1, 2, 3, 4, 5]))

def revList(arr):
    length = len(arr)
    for i in range(length-1, -1, -1):
        arr.append(arr.pop(i))
    return arr


# print(revList([1, 2, 3, 4, 5, 6]))
