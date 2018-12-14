aline_0 = {'color':'green', 'points':'5'}
print(aline_0['color'])
print(aline_0['points'])
aline_1 ={}
aline_1['x_position'] = 0
aline_1['y_position'] = 25
aline_1['speed'] = 'fastfast'
print(aline_1)
print('Original x position is ' + str(aline_1['x_position']))
print('Original y position is ' + str(aline_1['y_position']))

if aline_1['speed'] == 'slot':
    x_increment = 1
elif aline_1['speed'] == 'medium':
    x_increment = 5
else:
    x_increment = 10
aline_1['x_position'] = aline_1['x_position'] + x_increment
print('New x position is ' + str(aline_1['x_position']))
