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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ConvertTestCase("test_single_function"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="suite")
