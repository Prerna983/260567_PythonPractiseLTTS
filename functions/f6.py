import random


def rand():
    return random.randint(5, 10)


print("Random value between 5 and 10 are: ", rand(), rand(), rand(), sep=" ")


def rand1(x, y):
    return random.randint(x, y)


x, y = int(input("x= ")), int(input("y= "))
print("Random numbers between x and y are: ", rand1(x,y), rand1(x,y), rand1(x,y), sep="  ")
