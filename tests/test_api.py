"""Module for all unittests api"""

import unittest
from fastapi import testclient
from api import app

HOST = 'localhost:8000'
URL = "/kvur/"

client = testclient.TestClient(app=app)


class TestsKvUrAPI(unittest.TestCase):
    """Class for unittests API"""

    def test_api_three_is_zero(self):
        """Прямая параллельна оси"""

        a = 2
        b = 4
        c = -6
        d = 64
        x1 = 1
        x2 = -3
        string = "Дискриминант больше нуля, два корня"
        output = client.get(
            f"http://{HOST}{URL}?a={a_in}&b={b_in}&c={c_in}"
            ).json()
        count = 4

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