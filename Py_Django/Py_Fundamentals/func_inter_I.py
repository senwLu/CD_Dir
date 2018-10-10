import random


def randInt(min=0, max=100):
    fNum = ((max - min) * random.random()) + min
    return int(round(fNum))


# print(randInt(min=50, max=200))
