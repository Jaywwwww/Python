available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese', 'salt', 'sugar', 'tomato', 'apple')
requested_toppings = []
number = 1
for number in range(1, 4):
	available = False
	while (available == False):
		requested_topping = str(input('Please input what you want to add, max 3, this is the %s : ' % number))
		if requested_topping in requested_toppings:
			print('Sir you have input duplicate toppings, please input alternatives')
			continue
		if requested_topping in available_toppings:
			requested_toppings.append(requested_topping)
			available = True
			continue
		else:
			print('Sorry sir, what you have ordered is not available, please input alternatives')
			available = False
			continue
	number = number + 1
print('Please check what you want to add:')
print(requested_toppings)
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping + '.')
	else:
		print('Sorry, we don`t have ' + requested_topping + ',' + ' please contact our staff')
print('Just wait for few minutes, your Pizza will be ready soon!!!')
print('Great news! Finished pizza making!')