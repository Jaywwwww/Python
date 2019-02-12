import json



def get_new_favorite_number():
    file_name = 'favorite_numbers.json'
    number = input('Please input your favorite number: ')
    with open(file_name, 'w') as file_obj:
        json.dump(number, file_obj)
    return number

def read_stored_favorite_number():
    file_name = 'favorite_numbers.json'
    try:
        with open(file_name) as file_obj:
            number = json.load(file_obj)
    except FileNotFoundError:
        number = input('what is your favorite numbers!\n')
        with open(file_name, 'w') as file:
            json.dump(number, file)
        return number
    else:
        return number

number = read_stored_favorite_number()
answer = input('Is ' + number + " your favorite number? 'yes or no': ")
if answer == 'yes':
    print(number + ' is your favorite number!\n')
else:
    correct_number = get_new_favorite_number()
    print(correct_number + ' is your favorite number!\n')