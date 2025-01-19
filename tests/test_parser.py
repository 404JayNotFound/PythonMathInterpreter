import unittest
from math_interpreter.core.nodes import NumberNode, BinaryOpNode
from math_interpreter.core.parser import Parser

class TestParser(unittest.TestCase):

    def test_addition(self):
        tokens = [('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '4')]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertIsInstance(ast, BinaryOpNode)
        self.assertEqual(ast.left.value, 3)
        self.assertEqual(ast.operator, '+')
        self.assertEqual(ast.right.value, 4)

    def test_parentheses(self):
        tokens = [('LPAREN', '('), ('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '4'), ('RPAREN', ')')]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertIsInstance(ast, BinaryOpNode)
        self.assertEqual(ast.left.value, 3)
        self.assertEqual(ast.operator, '+')
        self.assertEqual(ast.right.value, 4)

    def test_pi_constant(self):
        tokens = [('PI', 'pi')]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertIsInstance(ast, NumberNode)
        self.assertEqual(ast.value, 3.141592653589793)

    def test_invalid_token(self):
        """Test invalid tokens."""
        tokens = [('NUMBER', '3'), ('PLUS', '+'), ('INVALID', 'abc')]
        parser = Parser(tokens)
        with self.assertRaises(ValueError):
            parser.parse()

    def test_mismatched_parentheses(self):
        """Test mismatched parentheses."""
        tokens = [('LPAREN', '('), ('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '4')]
        parser = Parser(tokens)
        with self.assertRaises(ValueError):
            parser.parse()

    def test_unexpected_token(self):
        """Test unexpected token."""
        tokens = [('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '4'), ('EOF', '')]
        parser = Parser(tokens)
        with self.assertRaises(ValueError):
            parser.parse()

if __name__ == "__main__":
    unittest.main()
