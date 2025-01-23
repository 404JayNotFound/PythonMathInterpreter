import unittest
from math_interpreter.core.lexer import tokenize

class TestLexer(unittest.TestCase):

    def test_single_number(self):
        tokens = list(tokenize("42"))
        self.assertEqual(tokens, [('NUMBER', 42.0)])

    def test_multiple_tokens(self):
        tokens = list(tokenize("42 + 3.14 * pi"))
        expected = [
            ('NUMBER', 42.0),
            ('PLUS', '+'),
            ('NUMBER', 3.14),
            ('TIMES', '*'),
            ('PI', 'pi')
        ]
        self.assertEqual(tokens, expected)

    def test_functions_and_parentheses(self):
        tokens = list(tokenize("sin(3) + cos(2)"))
        expected = [
            ('SIN', 'sin'),
            ('LPAREN', '('),
            ('NUMBER', 3.0),
            ('RPAREN', ')'),
            ('PLUS', '+'),
            ('COS', 'cos'),
            ('LPAREN', '('),
            ('NUMBER', 2.0),
            ('RPAREN', ')')
        ]
        self.assertEqual(tokens, expected)

    def test_exponent_and_sqrt(self):
        tokens = list(tokenize("2^3 + sqrt(4)"))
        expected = [
            ('NUMBER', 2.0),
            ('EXPONENT', '^'),
            ('NUMBER', 3.0),
            ('PLUS', '+'),
            ('SQRT', 'sqrt'),
            ('LPAREN', '('),
            ('NUMBER', 4.0),
            ('RPAREN', ')')
        ]
        self.assertEqual(tokens, expected)

    def test_inverse_trig_functions(self):
        """Test inverse trigonometric functions like asin, acos, atan."""
        tokens = list(tokenize("asin(0.5) + acos(1)"))
        expected = [
            ('ASIN', 'asin'),
            ('LPAREN', '('),
            ('NUMBER', 0.5),
            ('RPAREN', ')'),
            ('PLUS', '+'),
            ('ACOS', 'acos'),
            ('LPAREN', '('),
            ('NUMBER', 1.0),
            ('RPAREN', ')')
        ]
        self.assertEqual(tokens, expected)

        tokens = list(tokenize("atan(1)"))
        expected = [
            ('ATAN', 'atan'),
            ('LPAREN', '('),
            ('NUMBER', 1.0),
            ('RPAREN', ')')
        ]
        self.assertEqual(tokens, expected)

    def test_empty_string(self):
        """Test empty string returns an empty list of tokens."""
        tokens = list(tokenize(""))
        self.assertEqual(tokens, [])

    def test_whitespace_handling(self):
        """Test tokenization with leading, trailing, and multiple spaces."""
        tokens = list(tokenize("  42  +  3.14  *  pi   "))
        expected = [
            ('NUMBER', 42.0),
            ('PLUS', '+'),
            ('NUMBER', 3.14),
            ('TIMES', '*'),
            ('PI', 'pi')
        ]
        self.assertEqual(tokens, expected)

    def test_floating_point_numbers(self):
        """Test floating point numbers with multiple decimals and scientific notation."""
        tokens = list(tokenize("3.14159 + 2.5e3"))
        expected = [
            ('NUMBER', 3.14159),
            ('PLUS', '+'),
            ('NUMBER', 2.5),
            ('E', 'e'),
            ('NUMBER', 3.0)
        ]
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()