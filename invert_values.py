import unittest


def invert(lst):
    # tmp = []
    # for i in lst:
    #     if i <= 0:
    #         tmp.append(abs(i))
    #
    #     else:
    #         tmp.append(-i)

    # return [abs(i) if i <= 0 else -i for i in lst]
    return [-x for x in lst]


class InvertTest(unittest.TestCase):

    def test_invert(self):
        self.assertEqual(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
        self.assertEqual(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
        self.assertEqual(invert([1, -2, 0, -4, 5]), [-1, 2, 0, 4, -5])
        self.assertEqual(invert([]), [])

# python -m unittest -v invert_values.py
