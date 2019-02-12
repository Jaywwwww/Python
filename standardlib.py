from collections import OrderedDict

favorite_lauguages = OrderedDict()

favorite_lauguages['wujin'] = "C"
favorite_lauguages['liumengnan'] = "Python"

print(favorite_lauguages)

for name, lauguages in favorite_lauguages.items():
    print(name.title() + " `s favorite lauguages is " + lauguages.title() + ".")