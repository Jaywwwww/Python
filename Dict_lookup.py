rivers = {}
river = []
end = False
while end == False:
    river_name = input('Please input the river name:  ')
    country_name = input('Please input the country where the river goes through: ')
    rivers = {'river_name' : river_name , 'country_name' : country_name}
    river.append(rivers)
    print(rivers)
    flag = input('Do you want to add more? Yes or No? (default Yes)')
    if flag == 'yes':
        end = False
    elif flag == 'no':
        break
    else:
        end = False
print(rivers)
print(river)
for i in river:
    for rr, cc in i.items():
        print(rr + ': ' + cc)