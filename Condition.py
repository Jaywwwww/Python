name = input("please input your name:")
sex = input("please input your sex(male or female):")

while sex != "male" and sex != "female":
    print("error, sex is invalid, please input male or female")
    sex = input("please input your sex(male or female):")
age = int(input("please input your age:"))

if sex == "female" and age < 28:
    print("I love girls, come on to have a seat")
else:
    print("I don`t like you, you will be terminated")
