class Underscore:
    def map(self, arr, expression):
        result = []
        for i in arr:
            result.append(expression(i))
        return result

    def find(self, arr, expression):
        for i in arr:
            if expression(i):
                return i

    def filter(self, arr, expression):
        # your code
        result = []
        for i in arr:
            if expression(i):
                result.append(i)
        return result

    def reject(self, arr, expression):
        result = []
        for i in arr:
            if not expression(i):
                result.append(i)
        return result


# your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore()  # yes we are setting our instance to a variable that is an underscore

# should return [2,4,6]
test1 = _.map([1, 2, 3], lambda x: x*2)
# print(test1)

# should return the first value that is greater than 4
test2 = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
# print(test2)

# should return [2,4,6]
test3 = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print(test3)

# should return [1,3,5]
test4 = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(test4)
