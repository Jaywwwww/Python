alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print('you got 5 points')
if 'purple' in alien_color:
	print('you got 5 porints')
if 'green' in alien_color:
	print('you got 5 points since you killed aliens')
else:
	print('you got 10 points')
for alien in alien_color:
	if alien == 'green':
		print('you got 5 points since it is ' + alien)
	elif alien == 'yellow':
		print('you got 10 points since it is ' + alien)
	elif alien == 'red':
		print('you got 15 points since it is ' + alien)
age = int(input('please input you age: '))
if age < 0:
	print('Error, age cannot be less than 0')
elif age < 2:
	print('This is a baby')
elif age >= 2 and age < 4:
	print('He or she should be learning how to walk')
elif age >=4 and age < 13:
	print('This is a child')
elif age >= 13 and age < 20:
	print('This is a teenager')
elif age >= 20 and age < 65:
	print('This is a adult')
elif age >= 65 and age < 150:
	print('This is a older people')
else:
	print('Are you serious? Good bye')

