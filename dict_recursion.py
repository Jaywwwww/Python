alines = []
for aliens_number in range(10):
    new_aliens = {'speed' : 'slow', 'color' : 'green', 'point' : 5}
    alines.append(new_aliens)
for aliens_number in range(3):
    new_aliens = {'speed' : 'fast', 'color' : 'yellow', 'point': 6}
    alines.append(new_aliens)
for alien in alines[:]:
    print(alien)
print('...')
print('Showing how many aliens I have created: ' + str(len(alines)))
for alien in alines[:]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'Blue'
        alien['speed'] = 'Medium'
        alien['point'] = 8
print(alines)