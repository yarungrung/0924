# test_password_checker.py
import unittest
import re
from password_checker import generate_strong_password  # 修正匯入路徑

class TestGenerateStrongPassword(unittest.TestCase):
    def test_default_length(self):
        pwd = generate_strong_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        for length in [8, 16, 32]:
            pwd = generate_strong_password(length)
            self.assertEqual(len(pwd), length)

    def test_contains_lowercase(self):
        pwd = generate_strong_password()
        self.assertRegex(pwd, r'[a-z]')

    def test_contains_uppercase(self):
        pwd = generate_strong_password()
        self.assertRegex(pwd, r'[A-Z]')

    def test_contains_digit(self):
        pwd = generate_strong_password()
        self.assertRegex(pwd, r'\d')

    def test_contains_special(self):
        pwd = generate_strong_password()
        self.assertRegex(pwd, r'[!@#$%^&*(),.?":{}|<>]')

    def test_raises_value_error_for_short_length(self):
        with self.assertRaises(ValueError):
            generate_strong_password(7)

    def test_randomness(self):
        pwds = {generate_strong_password() for _ in range(10)}
        self.assertGreater(len(pwds), 1)

if __name__ == "__main__":
    unittest.main()