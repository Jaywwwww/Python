class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def read_car_info(self):
        full_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return full_name

    def read_odometer(self):
        print('This car has been running for ' + str(self.odometer) + ' kilometers')

    def set_odometer(self, kilometers):
        if kilometers >= self.odometer:
            self.odometer = kilometers
        else:
            print('Error! You cannot rollback the mileage!!!')

    def add_odometer(self, kilometers):
        if kilometers>=0:
            self.odometer += kilometers
        else:
            print('Error! Invalid value!!!')

mycar = Car('Ford', 'Kuga', '2016')
print(mycar.read_car_info())
mycar.read_odometer()
mycar.set_odometer(100)
mycar.read_odometer()
mycar.add_odometer(200)
mycar.read_odometer()
mycar.set_odometer(100)
mycar.read_odometer()
mycar.add_odometer(-1)
mycar.read_odometer()