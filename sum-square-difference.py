#!/bin/python3

import os, math

n=1
p=0
q=0

for n in range(1, 101):
    p+=n**2



for n in range(1, 101):
    q+=n

a=q**2

s=a-p

print(s)
