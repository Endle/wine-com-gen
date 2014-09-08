import sys
sys.path.append('../')

import unittest

import main
import TestTable

class ConvertTestCase(unittest.TestCase):
    def _test_table(self, func, table):
        for case in table:
            self.assertEqual(func(case[0]), case[1])
    def test_single_function(self):
        self._test_table(main.single_function, TestTable.TABLE_SINGLE_FUNCTION)
    def test_get_header(self):
        self._test_table(main.get_header, TestTable.TABLE_GET_HEADER)
    def test_get_parameter_list(self):
        self._test_table(main.get_parameter_list, TestTable.TABLE_GET_PARAMETER_LIST)
    def test_generate_FIXME(self):
        self._test_table(main.generate_FIXME, TestTable.TABLE_GENERATE_FIXME)


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
