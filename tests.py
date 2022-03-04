import unittest
from task import conv_num, conv_endian


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

    def test_7(self):
        input = "0xAZ4"
        expection = None
        self.assertEqual(conv_num(input), expection)

    def test_8(self):
        input = "12.3.45"
        expection = None
        self.assertEqual(conv_num(input), expection)

    def test_9(self):
        input = "12345A"
        expection = None
        self.assertEqual(conv_num(input), expection)


class TestFunction3(unittest.TestCase):

    # Basic tests
    def test_1(self):
        input = [954786, 'big']
        expection = '0E 91 A2'
        self.assertEqual(conv_endian(input[0], input[1]), expection)

    def test_2(self):
        input = 954786
        expection = '0E 91 A2'
        self.assertEqual(conv_endian(input), expection)

    def test_3(self):
        input = -954786
        expection = '-0E 91 A2'
        self.assertEqual(conv_endian(input), expection)

    def test_4(self):
        input = [954786, 'little']
        expection = 'A2 91 0E'
        self.assertEqual(conv_endian(input[0], input[1]), expection)

    def test_5(self):
        input = [-954786, 'little']
        expection = '-A2 91 0E'
        self.assertEqual(conv_endian(input[0], input[1]), expection)

    def test_6(self):
        expection = '-A2 91 0E'
        self.assertEqual(conv_endian(num=-954786, endian='little'), expection)

    def test_7(self):
        expection = None
        self.assertEqual(conv_endian(num=-954786, endian='small'), expection)

    # Random tests
    def test_8(self):
        expection = None
        self.assertEqual(conv_endian(num=-954786, endian='*$%'), expection)

    def test_9(self):
        expection = '-A2 91 0E'
        self.assertEqual(conv_endian(-954786, endian='little'), expection)

    def test_10(self):
        expection = None
        self.assertEqual(conv_endian(num=-954786, endian='Little'), expection)


if __name__ == '__main__':
    unittest.main()
