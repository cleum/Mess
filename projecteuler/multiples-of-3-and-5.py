import os, math


def mult(n):
    for i in range(3, 11):
        if ((n%3 == 0) or (n%5 == 0)):
            return n
        else: 
            return 0

sum=0

for i in range(3, 1000):
    sum+=mult(i)

print(sum)
