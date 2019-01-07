class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant name is ' + self.restaurant_name)
        print('This restaurant is ' + self.cuisine_type + ' flavor!')

    def open_restaurant(self):
        print('The restaurant is opening! Welcome!')

location = Restaurant('Peking Restaurant', 'Chinese Food')
location.describe_restaurant()
location.open_restaurant()
print(location.restaurant_name)
print(location.cuisine_type)