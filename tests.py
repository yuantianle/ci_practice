import unittest
from task import conv_num


class TestFunction1(unittest.TestCase):

    def test_1(self):
        input = "12345"
        expection = 12345
        self.assertEqual(conv_num(input), expection)

    def test_2(self):
        input = "-1234.5"
        expection = -1234.5
        self.assertEqual(conv_num(input), expection)

    def test_3(self):
        input = "-.45"
        expection = -0.45
        self.assertEqual(conv_num(input), expection)

    def test_4(self):
        input = "-123."
        expection = -123.0
        self.assertEqual(conv_num(input), expection)

    def test_5(self):
        input = "-0xAB"
        expection = -171
        self.assertEqual(conv_num(input), expection)

    def test_6(self):
        input = "-0XAb"
        expection = -171
        self.assertEqual(conv_num(input), expection)

class TestFunction3(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
