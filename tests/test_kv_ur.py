"""Module for all unittests
"""
import unittest
from main import kv_ur


class TestsKvUr(unittest.TestCase):
    """Class for unittests
    """
    def test_more_zero(self):
        """Test for discriminant more than zero
        """
        a = 2
        b = 4
        c = -6
        d = 64
        x1 = 1
        x2 = -3
        string = "Дискриминант больше нуля, два корня"
        count = 4
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), count,
                         "incorrect count of values (square equation)")
        self.assertEqual(output[0], string,
                         "incorrect string (square equation)")
        self.assertEqual(output[1], d,
                         "incorrect discriminant (square equation)")
        self.assertEqual(output[2], x1,
                         "incorrect x1 (square equation)")
        self.assertEqual(output[3], x2,
                         "incorrect x2 (square equation)")

    def test_linear_equation(self):
        """Test for linear equation
        """
        a = 0
        b = 2
        c = -4
        x = 2
        string = "Уравнение линейное, один корень"
        count = 2
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), count,
                         "incorrect count of values (linear equation)")
        self.assertEqual(output[0], string,
                         "incorrect string (linear equation)")
        self.assertEqual(output[1], x,
                         "incorrect x (linear equation)")
