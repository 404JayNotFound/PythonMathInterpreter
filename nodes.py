class NumberNode:
    def __init__(self, value):
        self.value = value

class FunctionCallNode:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class UnaryOpNode:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class VariableNode:
    def __init__(self, name):
        self.name = name
