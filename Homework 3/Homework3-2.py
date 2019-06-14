
"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 03
@date: 12/02/2019
@time: 08:09:57
This code Implements a class for fractions that supports addition, subtraction,
multiplication, and division
"""


import unittest

class Fraction:
    """ Support addition, subtraction, multiplication, and division of
    fractions
    with a simple algorithm
    """
    def __init__(self, num, denom):
        """ set num and denom
        Raise ValueError on 0 denominator
        """
        self.num = num
        self.denom = denom

        if denom == 0:
            raise ValueError('0 is an invalid denominator')

    def __str__(self):
        """ String to display fractions """
        return str(self.num) + '/' + str(self.denom)

    def __add__(self, other):
        """ Add two fractions using simplest approach """
        top = (self.num * other.denom) + (self.denom * other.num)
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = (self.num * other.denom) - (self.denom * other.num)
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __truediv__(self, other):
        return self.__mul__(Fraction(other.denom, other.num))

    def __eq__(self, other):
        """ return True/False if the two fractions are equivalent """
        return (self.num * other.denom) == (self.denom * other.num)

    def __ne__(self, other):  # Not equal
        return (self.num * other.denom) != (self.denom * other.num)

    def __lt__(self, other):  # less than
        return (self.num * other.denom) < (self.denom * other.num)

    def __le__(self, other):  # less than or equal to
        return (self.num * other.denom) <= (self.denom * other.num)

    def __gt__(self, other):  # greater than
        return (self.num * other.denom) > (self.denom * other.num)

    def __ge__(self, other):  # greater than or equal to
        return (self.num * other.denom) >= (self.denom * other.num)


class FractionTest(unittest.TestCase):
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)

    def test_str(self):
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')




    def test_not_equal(self):
        """test fraction non equality works"""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertFalse(f1 != f1)
        self.assertFalse(f1 != f2)
        self.assertFalse(f1 != f3)
        self.assertFalse(f2 != f3)
        self.assertTrue(f1 != Fraction(3, 5))
        self.assertTrue((f1+f3) != f2)
        self.assertFalse((f1+f2) != (f2+f1))

    def test_lessthan(self):
        """Test fraction less than works"""
        f1 = Fraction(4, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(12, 76)
        self.assertFalse(f1 < f1)
        self.assertFalse(f1 < f2)
        self.assertFalse(f1 < f3)
        self.assertTrue(f2 < f1)
        self.assertFalse(f2 < f2)
        self.assertFalse(f2 < f3)
        self.assertTrue(f3 < f1)
        self.assertTrue(f3 < f2)
        self.assertFalse(f3 < f3)
        self.assertFalse(f1 < Fraction(21, 96))
        self.assertFalse(f2 < Fraction(2, 16))
        self.assertFalse(f2 >= (f1+f3) and f3 < Fraction(5, 8) and f1==(16, 16))

    def test_lequal(self):
        """Test fraction less than or equal to works"""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(5, 9)
        self.assertTrue(f1 <= f1)
        self.assertTrue(f1 <= f2)
        self.assertFalse(f1 <= f3)
        self.assertTrue(f2 <= f1)
        self.assertTrue(f2 <= f2)
        self.assertFalse(f2 <= f3)
        self.assertTrue(f3 <= f1)
        self.assertTrue(f3 <= f2)
        self.assertTrue(f3 <= f3)
        self.assertFalse(f1 <= Fraction(3, 9))
        self.assertFalse(f2 <= Fraction(4, 8))
        self.assertTrue(f3 <= Fraction(7, 8))
        self.assertFalse((f1+f2)<=f3)

    def test_greater(self):
        """Test fraction greater than works"""
        f1 = Fraction(4, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(2, 3)
        self.assertFalse(f1 > f1)
        self.assertTrue(f1 > f2)
        self.assertTrue(f1 > f3)
        self.assertFalse(f2 > f1)
        self.assertFalse(f2 > f2)
        self.assertTrue(f2 > f3)
        self.assertFalse(f3 > f1)
        self.assertFalse(f3 > f2)
        self.assertFalse(f3 > f3)
        self.assertFalse(f1 > Fraction(6, 2))
        self.assertTrue((f1+f2-f3) > ((f3*f2)/f1))

    def test_gequal(self):
        """Test fraction greater than or equal to works"""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 7)
        self.assertTrue(f1 >= f1)
        self.assertTrue(f1 >= f2)
        self.assertFalse(f1 >= f3)
        self.assertTrue(f2 >= f1)
        self.assertTrue(f2 >= f2)
        self.assertFalse(f2 >= f3)
        self.assertTrue(f3 >= f1)
        self.assertTrue(f3 >= f2)
        self.assertTrue(f3 >= f3)
        self.assertFalse(f1 >= Fraction(4, 3))
        self.assertTrue((f1+f3) >= f2)

    def test_equal(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f1 == Fraction(3, 5))
        self.assertFalse((f1+f2) == f2 or (f1+f3) == f2 or (f2+f3) == f1)

    def test_div(self):
        """test fraction for division"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 7)
        self.assertFalse((f1 / f1) == Fraction(6, 4))
        self.assertFalse((f1 / f2) == Fraction(5, 4))
        self.assertFalse((f1 / f3) == Fraction(13, 12))
        """the below case is when the denominator is zero and gives ZeroDivisionError and points 
        in which function the error has occured, which is the main idea behind writing the test case"""
        #self.assertFalse(f1 / Fraction(0, 5))
        self.assertFalse(Fraction(154, 69) <= (f1+f2+f3))

    def test_mul(self):
        """test fraction for multiplication"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 7)
        self.assertFalse((f1 * f1) == Fraction(6, 4))
        self.assertTrue((f1 * f2) == Fraction(3, 8))
        self.assertFalse((f1 * f3) == Fraction(13, 12))
        self.assertTrue((f2 * f3) == (Fraction(2, 7) * Fraction(0.5, 2)))
        self.assertTrue((f2 * f3) >= (Fraction(2, 7) * Fraction(0.5, 2)))


    def test_sub(self):
        """ test fraction subtraction """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertFalse((f1 - f1) == Fraction(6, 4))
        self.assertFalse((f1 - f2) == Fraction(5, 4))
        self.assertFalse((f1 - f3) == Fraction(13, 12))
        self.assertTrue((f1-f2) < f3)

    def test_plus(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))
        self.assertFalse((f2+f3) <= f2)

    def testraise(self):
        """ Test for ValueError"""
        with self.assertRaises(ValueError):
            Fraction(99, 0)

if __name__ == '__main__':
# note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)





