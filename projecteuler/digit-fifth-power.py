#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

for i in range(10000, 100000):
    i=str(i)
    sum=int(i[0:1])**5 + int(i[1:2])**5 + int(i[2:3])**5 + int(i[3:4])**5 + int(i[4:5])**5

    if sum==i:
        print(sum, i)
