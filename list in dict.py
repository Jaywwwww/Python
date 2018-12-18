pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'pepper'],
    'flavors' : ['barbeque', 'chicken'],
    }
print(pizza)
for types, contents in pizza.items():
    if types == 'crust':
        print('The ' + types + ' is ' + contents + " style.")
    elif types == 'toppings' and len(contents) > 1:
        print('Added toppings are: ')
        for topping in pizza[types]:
            print(topping)
    elif types == 'toppings' and len(contents) == 1:
        print('Added extra '+ contents[0] + '.')
    elif types == 'flavors' and len(contents) > 1:
        print('The flavor are: ')
        for flavor in pizza[types]:
            print(flavor)
    elif types == 'flavors' and len(contents) == 1:
        print('The flavor is ' + contents[0])