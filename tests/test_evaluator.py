import unittest
import math
from math_interpreter.core.nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode, UnaryOpNode
from math_interpreter.core.evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    
    def setUp(self):
        """Set up the evaluator instance and shared variables."""
        self.evaluator = Evaluator()
        self.variables = {'x': 10, 'y': 5}
        self.evaluator.variables = self.variables

    def test_evaluate_number_node(self):
        """Test evaluation of NumberNode."""
        node = NumberNode(42)
        self.assertEqual(self.evaluator.evaluate(node), 42)

    def test_evaluate_binary_op_node(self):
        """Test evaluation of BinaryOpNode."""
        node = BinaryOpNode(
            left=NumberNode(3),
            operator='+',
            right=NumberNode(4)
        )
        self.assertEqual(self.evaluator.evaluate(node), 7)

    def test_evaluate_unary_op_node(self):
        """Test evaluation of UnaryOpNode."""
        node = UnaryOpNode(
            operator='-',
            operand=NumberNode(5)
        )
        self.assertEqual(self.evaluator.evaluate(node), -5)

    def test_evaluate_variable_node(self):
        """Test evaluation of VariableNode."""
        node = VariableNode('x')
        self.assertEqual(self.evaluator.evaluate(node), 10)

    def test_evaluate_function_call_node(self):
        """Test evaluation of FunctionCallNode."""
        node = FunctionCallNode(
            name='sqrt',
            arguments=[NumberNode(16)]
        )
        self.assertEqual(self.evaluator.evaluate(node), 4)

    def test_apply_operator(self):
        """Test binary operators."""
        self.assertEqual(self.evaluator.apply_operator('+', 1, 2), 3)
        self.assertEqual(self.evaluator.apply_operator('-', 5, 3), 2)
        self.assertEqual(self.evaluator.apply_operator('*', 4, 3), 12)
        self.assertEqual(self.evaluator.apply_operator('/', 10, 2), 5)
        self.assertEqual(self.evaluator.apply_operator('^', 2, 3), 8)

    def test_apply_unary_operator(self):
        """Test unary operators."""
        self.assertEqual(self.evaluator.apply_unary_operator('+', 10), 10)
        self.assertEqual(self.evaluator.apply_unary_operator('-', 10), -10)

    def test_apply_function(self):
        """Test mathematical functions."""
        self.assertEqual(self.evaluator.apply_function('sin', [math.pi / 2]), 1)
        self.assertEqual(self.evaluator.apply_function('cos', [0]), 1)
        self.assertEqual(self.evaluator.apply_function('tan', [0]), 0)
        self.assertEqual(self.evaluator.apply_function('sqrt', [25]), 5)

    def test_apply_inverse_trig_functions(self):
        """Test inverse trigonometric functions."""
 
        self.assertEqual(self.evaluator.apply_function('asin', [1]), math.pi / 2)
        self.assertEqual(self.evaluator.apply_function('asin', [-1]), -math.pi / 2)

        self.assertEqual(self.evaluator.apply_function('acos', [1]), 0)
        self.assertEqual(self.evaluator.apply_function('acos', [0]), math.pi / 2)

        self.assertEqual(self.evaluator.apply_function('atan', [0]), 0)
        self.assertEqual(self.evaluator.apply_function('atan', [1]), math.pi / 4)

    def test_invalid_inverse_trig_function(self):
        """Test invalid inputs for inverse trigonometric functions."""
        with self.assertRaises(ValueError):
            self.evaluator.apply_function('asin', [2])
        
        with self.assertRaises(ValueError):
            self.evaluator.apply_function('acos', [2])

    def test_invalid_binary_operator(self):
        """Test invalid binary operator."""
        with self.assertRaises(ValueError):
            self.evaluator.apply_operator('%', 2, 3)

    def test_invalid_unary_operator(self):
        """Test invalid unary operator."""
        with self.assertRaises(ValueError):
            self.evaluator.apply_unary_operator('~', 10)

    def test_invalid_function(self):
        """Test invalid function call."""
        with self.assertRaises(ValueError):
            self.evaluator.apply_function('unknown', [1])

    def test_divide_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ZeroDivisionError):
            self.evaluator.apply_operator('/', 10, 0)

    def test_function_with_invalid_argument(self):
        """Test function call with an invalid argument."""
        with self.assertRaises(ValueError):
            self.evaluator.apply_function('sqrt', [-1])

    def tearDown(self):
        """Clean up after each test."""
        pass

if __name__ == '__main__':
    unittest.main()