import os, math

readfile=open("large-sum.txt", 'r')

sum=0

for line in readfile :
    sum+=int(line)

print(sum)
