import os, math


def countdiv(n) :
    c=0
    for i in range(1, n) :
        if n%i == 0 :
            c=c+1
    return c

n=1
c=countdiv(n)

for n in range(1, 10) :
    print(c)
