#!/bin/python3

import os, math

n=1
fact=1

for n in range(1, 101):
    fact=fact*n
    print(fact)


sum=0

for i in str(fact):
    sum+=int(i)

print(sum)
