def accept_toppings(*toppings):
    print('This is what you have ordered')
    for topping in toppings:
        print(' - ' + topping)

def car_build(vendor, model, **car_info):
    car = {}
    car['vendor'] = vendor
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


accept_toppings('mushroom', 'fish', 'chicken')
car_sample1 = car_build('subaru' , 'outback' , color='red', tow_package = True)
print(car_sample1)