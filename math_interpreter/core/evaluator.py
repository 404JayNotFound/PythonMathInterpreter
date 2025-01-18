import math
from math_interpreter.core.nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode, UnaryOpNode

variables = {}

class Evaluator:
    def __init__(self, variables=None):
        """Initialize the evaluator with optional variables."""
        self.variables = variables if variables is not None else {}
        
    def evaluate(self, node):
        """Evaluate the AST node."""
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
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '^':
            return left ** right
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def apply_unary_operator(self, operator, operand):
        """Apply unary operators."""
        if operator == '+':
            return +operand
        elif operator == '-':
            return -operand
        else:
            raise ValueError(f"Unknown unary operator: {operator}")

    def apply_function(self, name, arguments):
        """Apply mathematical functions."""
        argument = arguments[0]
        
        if name == 'sin':
            return math.sin(argument)
        elif name == 'cos':
            return math.cos(argument)
        elif name == 'tan':
            return math.tan(argument)
        elif name == 'asin':
            return math.asin(argument)
        elif name == 'acos':
            return math.acos(argument)
        elif name == 'atan':
            return math.atan(argument)
        elif name == 'sqrt':
            return math.sqrt(argument)
        else:
            raise ValueError(f"Unknown function: {name}")
