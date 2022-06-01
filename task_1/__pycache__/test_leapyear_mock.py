from calendar import leapdays
import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
from leapyear import LeapYear
import leapyear

class TestMocking(unittest.TestCase):
    def test_mocking(self):
        mock_year = Mock()
        mock_year.method.return_value = 2000
        self.assertTrue(mock_year.method(),LeapYear.to_leap_year(2000))
        # print(mock_year.mock_calls)
        # mock_year.assert_called_with(2000)

    def test_non_integers(self):
        '''to_leap_year should fail with non-integer input'''
        mock_non_int = Mock()
        # mock_non_int.method.return_value = leapyear.NotIntegerError
        with self.assertRaises(TypeError):
            LeapYear.to_leap_year(0.5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    #unittest.main()