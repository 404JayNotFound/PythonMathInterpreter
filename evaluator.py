import math
from nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode

variables = {}

class Evaluator:
    def evaluate(self, node):
        """Evaluate the AST node."""
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, BinaryOpNode):
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)
            return self.apply_operator(node.operator, left_value, right_value)
        elif isinstance(node, VariableNode):
            return variables.get(node.name, 0)
        elif isinstance(node, FunctionCallNode):
            return self.apply_function(node.name, node.arguments)

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
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def apply_function(self, name, arguments):
        """Apply mathematical functions."""
        argument = self.evaluate(arguments[0])
        if name == 'sin':
            return math.sin(argument)
        elif name == 'cos':
            return math.cos(argument)
        elif name == 'tan':
            return math.tan(argument)
        elif name == 'log':
            return math.log(argument)
        else:
            raise ValueError(f"Unknown function: {name}")
