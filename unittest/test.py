import unittest

from isbn_validation import valid_ISBN10


class IsbnTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(valid_ISBN10('1112223339'), True)
        self.assertEqual(valid_ISBN10('048665088X'), True)
        self.assertEqual(valid_ISBN10('1293000000'), True)
        self.assertEqual(valid_ISBN10('1234554321'), True)
        print('test true')

    def test_false(self):
        self.assertEqual(valid_ISBN10('1234512345'), False)
        self.assertEqual(valid_ISBN10('1293'), False)
        self.assertEqual(valid_ISBN10('X123456788'), False)
        self.assertEqual(valid_ISBN10('ABCDEFGHIJ'), False)
        self.assertEqual(valid_ISBN10('XXXXXXXXXX'), False)
        print('test false')


if __name__ == '__main__':
    unittest.main()
