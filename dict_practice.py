allan = {'name' : 'allan', 'gender' : 'male', 'age' : 28}
terry = {'name' : 'terry', 'gender' : 'male', 'age' : 20}
tiffany = {'name' : 'tiffany', 'gender' : 'female', 'age' : 23}
people = [allan, terry, tiffany]
print(people)
for person in people:
    print('\nMy name is ' + person['name'])
    print('I am a ' + person['gender'])
    print('I am ' + str(person['age']) + ' years old')
    
favourite_place = {
    'clark' : ['beijing', 'new york', 'sydney'],
    'morrison' : ['los angeles', 'san fransisco'],
    'harry' : ['boston' , 'toronto', 'shanghai'],
    'mia' : ['wellington' , 'Roma']
}
for name, places in favourite_place.items():
    print('\nMy name is ' + name + '.')
    for place in places[:]:
        print('My favorite cities are ' + place)

