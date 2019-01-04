sandwich_orders = ['barbeque' , 'grill chicken' , 'cheese' , 'pastrami' , 'pastrami' , 'pastrami']
finished_sandwiches = []
print('Sorry, pastrami has been sold out!!!')
while sandwich_orders:
    while 'pastrami' in sandwich_orders:

        sandwich_orders.remove('pastrami')

    print('I made your tuna sandwich!')
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
for sandwich in finished_sandwiches:
    print('This is the sandwich you want: ' + sandwich)
