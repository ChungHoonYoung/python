import random as rd

lotto = []

while len(lotto) < 6 :
    num = rd.randint(1, 45)
    if num not in lotto :
        list.append(num)

print(lotto)
