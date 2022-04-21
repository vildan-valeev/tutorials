import unittest


def ips_between(start, end):
    # TODO
    return


class TestIps(unittest.TestCase):

    def test_ip(self):
        """"""

        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)
        self.assertEqual(ips_between("10.0.0.0", "10.0.1.0"), 256)

# python -m unittest -v count_ip_address.py
