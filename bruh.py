import os, math


def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return 0
    return n

n=3

for n in range(100, 1000) :
    if prime(n) == n:
        print(n, "est premier")
        rev=str(n)[::-1]
        if ((int(rev) > 99) and (int(rev) < 1001)) and (prime(int(rev)) == int(rev)) :
            print("L'inversion",rev,"de",n,"est également un nombre premier")
