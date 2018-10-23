import unittest

class testingStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEquals('gautham'.upper(),'GAUTHAM')

if __name__ == '__main__':
    unittest.main()