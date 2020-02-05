import os, math


def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return 0
    return n


sum=0

for i in range(2, 2000001):
    sum+=prime(i)

print(sum)
