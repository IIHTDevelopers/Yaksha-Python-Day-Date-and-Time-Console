import unittest
from dateandtime import date_time
from convertdays import convert_days
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_at_convert_days(self):
        test_obj = TestUtils()
        try:
            convert_days('5')
            test_obj.yakshaAssert("TestTypeErrorAtConvertDays", False, "exception")
            print("TestTypeErrorAtConvertDays = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorAtConvertDays", True, "exception")
            print("TestTypeErrorAtConvertDays = Passed")
