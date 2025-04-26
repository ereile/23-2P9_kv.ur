"""Module for all unittests"""

import unittest
from main import kv_ur


class TestsKvUr(unittest.TestCase):
    """Class for unittests"""

    def test_more_zero(self):
        """Дискрименант больше нуля"""
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

    def test_discriminant_is_zero(self):
        """Дискрименант равен нулю"""

        a = 3
        b = -18
        c = 27
        d = 0
        x = 3
        string = "Дискриминант равен нулю, один корень"
        z = 3
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), z, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорректна")
        self.assertEqual(output[1], d, "Дискриминант некорректен")
        self.assertEqual(output[2], x, "Корень некорректен")
    
    def test_linear_equation(self):
        """Прямая пересекает ось"""

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

    def test_three_is_zero(self):
        """Прямая параллельна оси"""

        a = 0
        b = 0
        c = 4
        answer = "Нет решения"
        string = "Линейное уравнение параллельное оси Ох"
        output = kv_ur(a, b, c)
        count = 2

        self.assertEqual(len(output), count, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорреткна")
        self.assertEqual(output[1], answer, "Ответ некорректен")

    def test_all_zero(self):
        """Прямая совпадает с осью"""

        a = 0
        b = 0
        c = 0
        linear_string = "Уравнение линейное"
        string = "Всё множество значений Ох"
        count = 2
        output = kv_ur(a, b, c)

        self.assertEqual(len(output), count, "incorrect count of values")
        self.assertEqual(output[0], linear_string, "incorrect string")
        self.assertEqual(output[1], string, "incorrect answer")
