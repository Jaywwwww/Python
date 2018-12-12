evennumbers = list(range(1, 22, 3))
print(evennumbers)
print(max(evennumbers))
print(min(evennumbers))
print(sum(evennumbers))
square = [value**2 for value in range(1, 11, 3)]
print(square)
print(square[2:4])
myfood = ['dumplings', 'bread', 'poridge']
print('my food is ')
print(myfood)
hisfood = myfood
herfood = myfood[:]
print(hisfood)
myfood.append('rice')
print(myfood)
print(hisfood)
print(herfood)
for food in myfood:
    print("my food is " + food)
