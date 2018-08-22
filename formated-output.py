name = input("name:")
age = input("age:")
job=input("job:")
hometown=input("hometown:")

print(type(name), type(age))

info = '''
----------info of %s-----------
       name is: %s               
       age is: %s                
       job is: %s                
       hometown is: %s           
-------------------------------
	''' % (name, name, age, job, hometown)

print(info)

name1=input("name1:")
name2=input("name2:")
info1 = "i want to confirm, %s is the most important to %s" % (name1,name2)
print(info1)