from unittest.mock import Mock
import unittest

import mock
import leapyear
from leapyear import LeapYear
import leapyear

class Test_smt(unittest.TestCase):
    def test_mocking(self):
        mock = Mock(spec=LeapYear)
        mock.to_leap_year(0.5)
        mock.assert_called_with(year = 0.5)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)