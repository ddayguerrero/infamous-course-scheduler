import unittest 
from unitTests import TestClass

suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
unittest.TextTestRunner(verbosity=2).run(suite)

test_register(__main__.TestClass, 'robert2', 'robert')

test_login(__main__.TestClass, 'robert', 'robert')

test_logout(__main__.TestClass)

test_student_lectures(__main__.TestClass, 2)

register_course(__main__.TestClass, 1)

delete_course(__main__.TestClass, 1)

test_student_fall_lectures(__main__.TestClass, 'COMP475')

test_student_winter_lectures(__main__.TestClass, 'COMP475')

test_student_summer_lectures(__main__.TestClass, 'COMP475')
