class Employee():
    def __init__(self, givenname, surename, salary):
        self.givenname = givenname
        self.surename = surename
        self.salary = salary
    def give_raise(self, salaryaddstep=5000):
        self.salary += salaryaddstep
        print('Salary has been added for ' + str(salaryaddstep) + ' , So your salary is now ' + str(self.salary))
    def read_employee_info(self):
        print(self.surename.title() + ' ' +self.givenname.title() + ' `s salary is ' + str(self.salary))

#wujin = Employee('jin', 'wu', 200000)
#wujin.read_employee_info()
#wujin.give_raise()
#wujin.read_employee_info()
#print(str(wujin.salary))