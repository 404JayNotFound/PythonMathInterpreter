import math
from math_interpreter.core.nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode, UnaryOpNode

variables = {}

class Evaluator:
    def __init__(self, variables=None):
        """Initialize the evaluator with variables."""
        self.variables = variables if variables is not None else {}

        self.operators = {
            '+': lambda left, right: left + right,
            '-': lambda left, right: left - right,
            '*': lambda left, right: left * right,
            '/': lambda left, right: left / right,
            '^': lambda left, right: left ** right,
        }
        
        self.unary_operators = {
            '+': lambda operand: +operand,
            '-': lambda operand: -operand,
        }
        
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sqrt': math.sqrt,
        }

    def evaluate(self, node):
        """Evaluate the expression tree."""
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, BinaryOpNode):
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)
            return self.apply_operator(node.operator, left_value, right_value)
        elif isinstance(node, UnaryOpNode):
            value = self.evaluate(node.operand)
            return self.apply_unary_operator(node.operator, value)
        elif isinstance(node, VariableNode):
            return self.variables.get(node.name, 0)
        elif isinstance(node, FunctionCallNode):
            evaluated_args = [self.evaluate(arg) for arg in node.arguments]
            return self.apply_function(node.name, evaluated_args)

    def apply_operator(self, operator, left, right):
        """Apply binary operators."""
        if operator not in self.operators:
            raise ValueError(f"Unknown operator: {operator}")
        return self.operators[operator](left, right)

    def apply_unary_operator(self, operator, operand):
        """Apply unary operators."""
        if operator not in self.unary_operators:
            raise ValueError(f"Unknown unary operator: {operator}")
        return self.unary_operators[operator](operand)

    def apply_function(self, name, arguments):
        """Apply mathematical functions."""
        if name not in self.functions:
            raise ValueError(f"Unknown function: {name}")
        if len(arguments) != 1:
            raise ValueError(f"Function {name} expects exactly one argument.")
        return self.functions[name](arguments[0])