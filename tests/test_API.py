"""Module for all unittests API"""

import unittest
import requests

HOST = 'localhost:8000'
URL = "/kvur/"


class TestsKvUrAPI(unittest.TestCase):
    """Class for unittests API"""

    def test_three_is_zero(self):
        """Прямая параллельна оси"""

        a = 0
        b = 0
        c = 4
        answer = "Нет решения"
        string = "Линейное уравнение параллельное оси Ох"
        output = requests.get(
            f"http://{HOST}{URL}?a={a}&b={b}&c={c}"
            ).json()
        count = 2

        self.assertEqual(len(output), count, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорреткна")
        self.assertEqual(output[1], answer, "Ответ некорректен")
