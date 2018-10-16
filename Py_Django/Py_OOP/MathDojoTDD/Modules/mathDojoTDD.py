class MathDojo:
    def __init__(self):
        self.sum = 0

    def add(self, num, *nums):
        add = num
        for i in range(len(nums)):
            add += nums[i]
        # return self.sum
        return self.sum

    def subtract(self, num, *nums):
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
        self.sum -= (num + sub)
        return self.sum

    def result(self):
        return self.sum
