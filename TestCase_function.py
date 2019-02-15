from fuction import get_formated
import unittest

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted = get_formated('wu', 'jin')
        self.assertEqual(formatted, 'Wu Jin')
    def test_first_middle_last_name(self):
        formatted = get_formated('Chris', 'jin' , 'sunny')
        self.assertEqual(formatted, 'Chris Sunny Jin')

if __name__ == '__main__':
    unittest.main()
