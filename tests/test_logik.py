"""Тесты для дискриминанта"""
import unittest
from main import kv_ur


class Tests(unittest.TestCase):
    """Класс тест"""
    def test_discriminant_is_zero(self):
        """Тесты для дискриминанта равная нулю"""
        a = 3
        b = -18
        c = 27
        d = 0
        x = 3
        string = "Дискриминант равен нулю, один корень"
        output = kv_ur(a, b, c)

        self.assertEqual(output[0], string, "Строка некорректна")
        self.assertEqual(output[1], d, "Дискриминант некорректен")
        self.assertEqual(output[2], x, "Корень некорректен")
