import unittest


# def reverseList(list):
#     if(len(list) == 0):
#         return "empty"
#     else:
#         for i in range(int(len(list)/2)):
#             list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
#         return list


# class isReverseTest(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(reverseList([1, 9, 4, 5, 2]), [2, 5, 4, 9, 1])

#     def testTwo(self):
#         self.assertEqual(reverseList([1, 2, 3]), [3, 2, 1])

#     def testThree(self):
#         self.assertEqual(reverseList([1, 1, 1]), [1, 1, 1])

#     def testFour(self):
#         self.assertEqual(reverseList([]), 'empty')

########################################################################


# def coins(centsGiven):
#     arr = []
#     q = 0
#     d = 0
#     n = 0
#     p = 0
#     if centsGiven == 0:
#         arr.append(q)
#         arr.append(d)
#         arr.append(n)
#         arr.append(p)
#     else:
#         while centsGiven >= 25:
#             q += 1
#             centsGiven -= 25
#         while centsGiven >= 10:
#             d += 1
#             centsGiven -= 10
#         while centsGiven >= 5:
#             n += 1
#             centsGiven -= 5
#         while centsGiven >= 1:
#             p += 1
#             centsGiven -= 1
#         arr.append(q)
#         arr.append(d)
#         arr.append(n)
#         arr.append(p)
#     return arr


# class coinTest(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(coins(87), [3, 1, 0, 2])

#     def testTwo(self):
#         self.assertEqual(coins(92), [3, 1, 1, 2])

#     def testThree(self):
#         self.assertEqual(coins(25), [1, 0, 0, 0])

#     def testFour(self):
#         self.assertEqual(coins(3), [0, 0, 0, 3])

#     def testFive(self):
#         self.assertEqual(coins(0), [0, 0, 0, 0])

########################################################################

def insert_val_at(val, insert_index, arr):

    if insert_index > len(arr)-1:
        for i in range(len(arr), insert_index):
            arr.append(0)
        arr.append(val)
    else:
        for i in range(insert_index, len(arr)):
            arr[i], val = val, arr[i]
            if i == len(arr)-1:
                arr.append(val)
    return arr


class insertValTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(insert_val_at(10, 3, [1, 3, 2, 5]), [1, 3, 2, 10, 5])

    def testTwo(self):
        self.assertEqual(insert_val_at(5, 0, [1, 3, 2, 5]), [5, 1, 3, 2, 5])

    def testThree(self):
        self.assertEqual(insert_val_at(4, 4, [1, 3]), [1, 3, 0, 0, 4])


if __name__ == '__main__':
    unittest.main()
