import unittest
from Class_Employee import Employee

class TestCase_Class_Employee(unittest.TestCase):
    def setUp(self):
        self.wujin = Employee('jin', 'wu', 10000)
        self.liumengnan = Employee('mengnan', 'liu', 20000)
        self.Cola = Employee('Cola', 'little', 3000)
    def test_default_give_raise(self):
        self.wujin.read_employee_info()
        self.wujin.give_raise()
        self.wujin.read_employee_info()
        self.assertEqual('15000', str(self.wujin.salary))
    def test_custom_give_raise(self):
        self.wujin.read_employee_info()
        self.wujin.give_raise(2000)
        self.wujin.read_employee_info()
        self.assertEqual('12000', str(self.wujin.salary))


if __name__ == '__main__':
    unittest.main()
