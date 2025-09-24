# test_password_checker.py
import unittest
from workspaces_0924.password_checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_empty_password(self):
        self.assertEqual(check_password_strength(""), "弱")

    def test_short_password(self):
        self.assertEqual(check_password_strength("abc"), "弱")

    def test_only_digits(self):
        self.assertEqual(check_password_strength("12345678"), "中等")  # length + digit

    def test_only_uppercase(self):
        self.assertEqual(check_password_strength("ABCDEFGH"), "中等")  # length + uppercase

    def test_only_lowercase(self):
        self.assertEqual(check_password_strength("abcdefgh"), "中等")  # length + lowercase

    def test_only_special_chars(self):
        self.assertEqual(check_password_strength("!@#$%^&*"), "中等")  # length + special

    def test_length_and_digit_and_uppercase(self):
        self.assertEqual(check_password_strength("A2345678"), "中等")  # length + digit + uppercase

    def test_length_digit_uppercase_lowercase(self):
        self.assertEqual(check_password_strength("Abc12345"), "中等")  # length + digit + uppercase + lowercase

    def test_length_digit_uppercase_lowercase_special(self):
        self.assertEqual(check_password_strength("Abc12345!"), "強")  # all rules

    def test_no_length_but_all_other_rules(self):
        self.assertEqual(check_password_strength("A1b!"), "中等")  # digit + uppercase + lowercase + special

    def test_score_boundaries(self):
        self.assertEqual(check_password_strength("abc12345"), "中等")  # length + digit + lowercase
        self.assertEqual(check_password_strength("Abc12345!"), "強")  # all rules

    def test_multiple_special_chars(self):
        self.assertEqual(check_password_strength("Abc12345!!!"), "強")

    def test_non_ascii_characters(self):
        self.assertEqual(check_password_strength("密码123A!a"), "強")  # length + digit + uppercase + lowercase + special

if __name__ == "__main__":
    unittest.main()