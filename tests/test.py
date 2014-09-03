import sys
sys.path.append('../')

import unittest

import main
import TestTable

class ConvertTestCase(unittest.TestCase):
    def test_single_function(self):
        for case in TestTable.TABLE_SINGLE_FUNCTION:
            self.assertEqual(main.single_function(case[0]), case[1])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ConvertTestCase("test_single_function"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="suite")
