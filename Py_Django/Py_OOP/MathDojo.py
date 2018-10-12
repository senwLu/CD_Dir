class MathDojo:
    def __init__(self):
        self.sum = 0

    def add(self, num, *nums):
        add = 0
        for i in range(len(nums)):
            add += nums[i]
        self.sum += (num + add)
        return self

    def subtract(self, num, *nums):
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
        self.sum -= (num + sub)
        return self

    def result(self):
        return self.sum


md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result()
print(x)
