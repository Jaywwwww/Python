class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('Lucky', 1)
your_dog = Dog('Happy', 2)
print(my_dog.name + ' is ' + str(my_dog.age) + ' years old')
print(your_dog.name + ' is ' + str(your_dog.age) + ' years old')
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()