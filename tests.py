import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test_1(self):
        input = "12345"
        expection = 12345
        self.assertEqual(conv_num(input), expection)

    def test_2(self):
        input = "-1234.5"
        expection = -1234.5
        self.assertEqual(conv_num(input), expection)


if __name__ == '__main__':
    unittest.main()
