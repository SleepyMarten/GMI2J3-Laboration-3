import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
import roman1

class TestMocking(unittest.TestCase):
    def test_mocking(self):
        #Create mock obj
        mock_year = Mock()
        mock_year.method.return_value = 2000
        self.assertTrue(mock_year.method(),LeapYear.to_leap_year(2000))
        # print(mock_year.mock_calls)
        # mock_year.assert_called_with(2000)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    #unittest.main()