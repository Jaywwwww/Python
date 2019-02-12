print("Give me two numbers, I will help you to divide them")
print("Enter 'q' to quit.\n")

while True:
    first_number = input("Please input the first number!\n")
    if first_number == 'q':
        break
    second_number = input("Please input the second number!\n")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!\n")
    else:
        print('%.2f' % answer)