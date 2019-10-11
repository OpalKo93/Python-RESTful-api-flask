import app
from arithmetic import sum_strings, mul_strings
from unittest import TestCase


class TestSumMul(TestCase):
    def test_sum_result(self):
        num1 = "32"
        num2 = "13"
        expected_result = [4, 5]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_carry_out(self):
        num1 = "999"
        num2 = "1"
        expected_result = [1, 0, 0, 0]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_zero(self):
        num1 = "999"
        num2 = "0"
        expected_result = [9, 9, 9]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_big_nums(self):
        num1 = "81241251325"
        num2 = "99999999999"
        expected_result = [1, 8, 1,2, 4, 1,2, 5, 1, 3, 2, 4]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_mul_result(self):
        num1 = "22"
        num2 = "4"
        expected_result = [8, 8]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_with_zero(self):
        num1 = "0"
        num2 = "3432432"
        expected_result = [0]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_with_carry_out(self):
        num1 = "11"
        num2 = "11"
        expected_result = [1, 2, 1]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_big_nums(self):
        num1 = "999"
        num2 = "999"
        expected_result = [9, 9, 8, 0, 0, 1]
        self.assertEqual(mul_strings(num1, num2), expected_result)




