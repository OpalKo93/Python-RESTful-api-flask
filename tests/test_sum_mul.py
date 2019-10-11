from arithmetic import sum_strings, mul_strings
from unittest import TestCase


class TestSumMul(TestCase):
    def test_sum_result(self):
        num1 = "32"
        num2 = "13"
        expected_result = [4, 5]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_none1(self):
        num1 = ""
        num2 = "537"
        expected_result = [5, 3, 7]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_none2(self):
        num1 = "321"
        num2 = ""
        expected_result = [3, 2, 1]
        self.assertEqual(sum_strings(num1, num2), expected_result)

    def test_sum_with_both_none(self):
        num1 = ""
        num2 = ""
        expected_result = []
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
        num1 = "8124125132532423432431433426362143342174"
        num2 = "999999243279636214334217481"
        expected_result = [8, 1, 2, 4, 1, 2, 5, 1, 3, 2, 5, 3, 3, 4, 2, 3, 4, 3, 1, 6, 7, 4, 7, 1, 3, 0, 6, 2, 5, 7, 6, 4, 7, 7, 5, 5, 9, 6, 5, 5]
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
        num1 = "9934543747312321466784252345265479"
        num2 = "1241312898745643999"
        expected_result = [1, 2, 3, 3, 1, 8, 7, 7, 2, 9, 6, 6, 9, 1, 6, 7, 0, 3, 9, 9, 0, 2, 7, 9, 7, 5, 8, 9, 9, 9, 3, 1, 3, 4, 3, 9, 0, 5, 7, 9, 7, 0, 2, 2, 4, 7, 8, 2, 1, 0, 5, 2, 1]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_with_none1(self):
        num1 = ""
        num2 = "321"
        expected_result = [3, 2, 1]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_with_none2(self):
        num1 = "321"
        num2 = ""
        expected_result = [3, 2, 1]
        self.assertEqual(mul_strings(num1, num2), expected_result)

    def test_mul_with_both_none(self):
        num1 = ""
        num2 = ""
        expected_result = []
        self.assertEqual(mul_strings(num1, num2), expected_result)

