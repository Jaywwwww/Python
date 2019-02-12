file_name = 'write_file.txt'
with open(file_name,'w') as file:
    file.write('I am a little boy\n')
    file.write('I love girls\n')

with open(file_name, 'a') as file:
    file.write('I am also a Engineer\n')
    file.write('I am also a network engineer\n')