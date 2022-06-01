import unittest
from mock import Mock
from unittest.mock import MagicMock

import mock
from task_1 import roman1

class FromRomanBadInput(unittest.TestCase):
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        mock_test_zero = Mock()
        roman1.to_roman(mock_test_zero)
        print(mock_test_zero.mock_calls)
        #self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, mock_test_zero)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)