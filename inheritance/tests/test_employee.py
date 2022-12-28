import unittest
from Employee import Employee



class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee('Samuel', 'Ohiri', 60000)
        self.employee_2 = Employee('Akin1', 'Bello', 80000)

    def tearDown(self) -> None:
        pass

    def test_email(self):

        self.assertEqual(self.employee_1.email, 'Samuel.Ohiri@email.com')
        self.assertEqual(self.employee_2.email, 'Akin1.Bello@email.com')

        self.employee_1.first = 'Chimezie'
        self.employee_2.first = 'Akinwunmi'

        self.assertEqual(self.employee_1.email, 'Chimezie.Ohiri@email.com')
        self.assertEqual(self.employee_2.email, 'Akinwunmi.Bello@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee_1.fullname, 'Samuel Ohiri')
        self.assertEqual(self.employee_2.fullname, 'Akin1 Bello')

        self.employee_1.first = 'Chimezie'
        self.employee_2.first = 'Akinwunmi'

        self.assertEqual(self.employee_1.fullname, 'Chimezie Ohiri')
        self.assertEqual(self.employee_2.fullname, 'Akinwunmi Bello')

    def test_pay_raise(self):

        self.assertEqual(self.employee_1.email, 'Samuel.Ohiri@email.com')
        self.assertEqual(self.employee_2.email, 'Akin1.Bello@email.com')

        self.employee_1.pay_raise()
        self.employee_2.pay_raise()

        self.assertEqual(self.employee_1.pay, 63000)
        self.assertEqual(self.employee_2.pay, 84000)
