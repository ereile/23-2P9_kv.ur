"""Module for all unittests api"""

import unittest
import requests

HOST = 'localhost:8000'
URL = "/kvur/"


class TestsKvUrAPI(unittest.TestCase):
    """Class for unittests API"""

    def test_api_three_is_zero(self):
        """Прямая параллельна оси"""

        a_in = 0
        b_in = 0
        c_in = 4
        answer = "Нет решения"
        string = "Линейное уравнение параллельное оси Ох"
        output = requests.get(
            f"http://{HOST}{URL}?a={a_in}&b={b_in}&c={c_in}",
            timeout=1000
            ).json()
        count = 2

        self.assertEqual(len(output), count, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорреткна")
        self.assertEqual(output[1], answer, "Ответ некорректен")
