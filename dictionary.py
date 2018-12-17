aline_0 = {'color':'green', 'points':'5'}
print(aline_0['color'])
print(aline_0['points'])
aline_1 ={}
aline_1['x_position'] = 0
aline_1['y_position'] = 25
aline_1['speed'] = 'fastfast'
print(aline_1)
print('Original x position is ' + str(aline_1['x_position']))
print('Original y position is ' + str(aline_1['y_position']))

if aline_1['speed'] == 'slot':
    x_increment = 1
elif aline_1['speed'] == 'medium':
    x_increment = 5
else:
    x_increment = 10
aline_1['x_position'] = aline_1['x_position'] + x_increment
print('New x position is ' + str(aline_1['x_position']))
print('Below is dictionary testing')
friends = {
    'first_name' : 'Micheal',
    'last_name' : 'Jordan',
    'age' : 36,
    'city' : 'New York',
}
print('My friend`s first name is ' + friends['first_name'])
print('His last name is ' + friends['last_name'])
print('His age is ' + str(friends['age']) + ' years old')
print('He located at ' + friends['city'])
favorite_digits = {
    'John' : 'red',
    'Terry' : 'green',
    'Harry' : 'purple',
    'Ted' : 'red',
    'Lily' : 'blue',
}
#names = input('Please input the name whom you want to know more: ')
for name, color in favorite_digits.items():
    print('\nKey: ' + name)
    print('value: ' + color)
    #if name == names:
        #print(name + ' `s favorite color is ' + color)
for name in favorite_digits.keys():
    print(name.title())
for color in favorite_digits.values():
    print(color)
print(favorite_digits.keys())
print(favorite_digits.items())
print(favorite_digits.values())
print(set(favorite_digits.values()))

