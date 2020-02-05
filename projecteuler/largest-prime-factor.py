import os, math


def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return 0
    return n

number=13195
