import unittest
from control import queryOrdersByDate

class queryOrderTest(unittest.TestCase):
    def test_queryOrderByDate_InvalidDate(self):
        result =queryOrdersByDate("YYYY-MM-DD")
        self.assertEqual(result, {})
    
    def test_queryOrderByDate_ValidDate_Empty(self):
        result = queryOrdersByDate("2020-01-01")
        self.assertEqual(result, {})

    def test_queryOrderByDate_ValidDate_NotEmpty(self):
        result = queryOrdersByDate("2019-08-03")
        resultHasKeys = len(result.keys()) > 0
        self.assertEqual( resultHasKeys, True)

if __name__ == "__main__":
    unittest.main()
