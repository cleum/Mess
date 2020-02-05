import os, math

number=2520

while True :
    verif=0
    for i in range(1, 21) :
        if number%i != 0 :
            break
        else :
            verif=verif+1

    if verif == 20 :
        break

    number=number+1

print(number)
