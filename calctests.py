import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.multiply(3, 5), 15)

    def test_sin(self):
        c = Calculator()
        self.assertEqual(c.sin(4), -0.7568024953)

    def test_cos(self):
        c = Calculator()
        self.assertEqual(c.cos(5), 0.28366218546)

    def test_tan(self):
        c = Calculator()
        self.assertEqual(c.tan(4), 1.15782128235)

    def test_inv_sin(self):
        c = Calculator()
        self.assertEqual(c.inv_sin(5), "Error")

    def test_inv_cos(self):
        c = Calculator()
        self.assertEqual(c.inv_cos(5), "Error")

    def test_inv_cos1(self):
        c = Calculator()
        self.assertEqual(c.inv_cos(1), 0)

    def test_inv_sin1(self):
        c = Calculator()
        self.assertEqual(c.inv_sin(1.0), 1.57079632679)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_div1(self):
        c = Calculator()
        self.assertEqual(c.divide(9, 3), 3)
    def test_div2(self):
        c = Calculator()
        self.assertEqual(c.divide(6, 6), 1)
    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3 ), 9)
    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 13), -4)
    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 13), -4)
    def test_divide1(self):
        c = Calculator()
        self.assertEqual(c.divide(9, 3), 3)
    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3 ), 9)

    def test_square1(self):
        c = Calculator()
        self.assertEqual(c.square(8), 64)

    def test_square_root(self):
        c = Calculator()
        self.assertEqual(c.square_root(9), 3)

    def test_exponentiate(self):
        c = Calculator()
        self.assertEqual(c.exponentiate(2 , 4), 16)

    def test_exponentiate1(self):
        c = Calculator()
        self.assertEqual(c.exponentiate(8, 4), 4096)

    def test_inverse(self):
        c = Calculator()
        self.assertEqual(c.inverse(-8), -1/8)

    def test_inverse1(self):
        c = Calculator()
        self.assertEqual(c.inverse(8), 1/8)

    def test_invert(self):
        c = Calculator()
        self.assertEqual(c.invert(8), -8)

    def test_invert1(self):
        c = Calculator()
        self.assertEqual(c.invert(-16), 16)

    def test_SwitchUnitsMode(self):
        c = Calculator()
        self.assertEqual(c.SwitchUnitsMode(1, "radian"), 0.0174533)

    def test_SwitchUnitsMode1(self):
        c = Calculator()
        self.assertEqual(c.SwitchUnitsMode(1, "degree"), 57.2957795)
if __name__ == '__main__':
    unittest.main()
