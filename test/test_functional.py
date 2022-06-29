import unittest
from dateandtime import date_time
from convertdays import convert_days
import datetime
now = datetime.datetime.now()
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_result_of_convert_days(self):
        test_obj = TestUtils()
        result=convert_days(50)
        if result==[0,7,1]:
            test_obj.yakshaAssert("TestResultOfConvertDays", True, "functional")
            print("TestResultOfConvertDays = Passed")
        else:
            test_obj.yakshaAssert("TestResultOfConvertDays", False, "functional")
            print("TestResultOfConvertDays = Failed")

    def test_result_of_convert_days_367(self):
        test_obj = TestUtils()
        result=convert_days(367)
        if result==[1,0,2]:
            test_obj.yakshaAssert("TestResultOfConvertDays367", True, "functional")
            print("TestResultOfConvertDays367 = Passed")
        else:
            test_obj.yakshaAssert("TestResultOfConvertDays367", False, "functional")
            print("TestResultOfConvertDays367 = Failed")

    def test_return_type_of_convert_days(self):
        test_obj = TestUtils()
        result=convert_days(300)
        if type(result)==type([]):
            test_obj.yakshaAssert("TestReturnTypeOfConvertDays", True, "functional")
            print("TestReturnTypeOfConvertDays = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeOfConvertDays", False, "functional")
            print("TestReturnTypeOfConvertDays = Failed")

    def test_current_date(self):
        test_obj = TestUtils()
        result=date_time(1)
        if result==now.strftime('%d-%m-%Y'):
            test_obj.yakshaAssert("TestCurrentDate", True, "functional")
            print("TestCurrentDate = Passed")
        else:
            test_obj.yakshaAssert("TestCurrentDate", False, "functional")
            print("TestCurrentDate = Failed")

    def test_current_date_format(self):
        test_obj = TestUtils()
        result=date_time(2)
        if result==now.strftime('%A, %B %d, %Y'):
            test_obj.yakshaAssert("TestCurrentDateFormat", True, "functional")
            print("TestCurrentDateFormat = Passed")
        else:
            test_obj.yakshaAssert("TestCurrentDateFormat", False, "functional")
            print("TestCurrentDateFormat = Failed")

    def test_current_date_format2(self):
        test_obj = TestUtils()
        result=date_time(3)
        if result==now.strftime('%x'):
            test_obj.yakshaAssert("TestCurrentDateFormat2", True, "functional")
            print("TestCurrentDateFormat2 = Passed")
        else:
            test_obj.yakshaAssert("TestCurrentDateFormat2", False, "functional")
            print("TestCurrentDateFormat2 = Failed")

    def test_current_time(self):
        test_obj = TestUtils()
        result=date_time(4)
        if result==now.strftime('%X'):
            test_obj.yakshaAssert("TestCurrentTime", True, "functional")
            print("TestCurrentTime = Passed")
        else:
            test_obj.yakshaAssert("TestCurrentTime", False, "functional")
            print("TestCurrentTime = Failed")

    def test_current_time_AM_PM(self):
        test_obj = TestUtils()
        result=date_time(5)
        if result==now.strftime('%p'):
            test_obj.yakshaAssert("TestCurrentTimeAMPM", True, "functional")
            print("TestCurrentTimeAMPM = Passed")
        else:
            test_obj.yakshaAssert("TestCurrentTimeAMPM", False, "functional")
            print("TestCurrentTimeAMPM = Failed")
