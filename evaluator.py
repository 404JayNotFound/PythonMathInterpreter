from math import sin, cos, tan
import math

from nodes import NumberNode, BinaryOpNode, UnaryOpNode, VariableNode, FunctionCallNode
variables={}


class Evaluator:
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
        elif operator == '**':
            return left ** right
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def apply_unary_operator(self, operator, value):
        """Apply unary operators."""
        if operator == 'abs':
            return abs(value)
        elif operator == 'sqrt':
            return math.sqrt(value)
        elif operator == 'log':
            return math.log10(value)
        else:
            raise ValueError(f"Unknown unary operator: {operator}")

    def apply_function(self, name, arguments):
        """Apply mathematical functions."""
        if name == 'sin':
            return math.sin(arguments[0])
        elif name == 'cos':
            return math.cos(arguments[0])
        elif name == 'tan':
            return math.tan(arguments[0])
        elif name == 'log':
            return math.log(arguments[0])
        else:
            raise ValueError(f"Unknown function: {name}")

    def evaluate(self, node):
        if node[0] == 'NUMBER':
            return node[1]
        
        elif node[0] == 'ADD':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left + right
        
        elif node[0] == 'SUB':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left - right
        
        elif node[0] == 'MUL':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left * right
        
        elif node[0] == 'DIV':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        
        elif node[0] == 'SIN':
            argument = self.evaluate(node[1])
            return sin(argument)
        
        elif node[0] == 'COS':
            argument = self.evaluate(node[1])
            return cos(argument)
        
        elif node[0] == 'TAN':
            argument = self.evaluate(node[1])
            return tan(argument)
        
        raise ValueError("Invalid node type: " + node[0])
