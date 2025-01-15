import math
from math_interpreter.core.nodes import NumberNode, BinaryOpNode, FunctionCallNode, VariableNode, UnaryOpNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        """Parse the list of tokens into an Abstract Syntax Tree (AST)."""
        return self.expression()

    def expression(self):
        """Handle addition and subtraction."""
        node = self.term()
        while self.current_token() and self.current_token()[0] in ['PLUS', 'MINUS']:
            op = self.consume()[1]
            right = self.term()
            node = BinaryOpNode(node, op, right)
        return node

    def term(self):
        """Handle multiplication and division."""
        node = self.exponent()
        while self.current_token() and self.current_token()[0] in ['TIMES', 'DIVIDE']:
            op = self.consume()[1]
            right = self.exponent()
            node = BinaryOpNode(node, op, right)
        return node

    def exponent(self):
        """Handle exponentiation."""
        node = self.factor()
        while self.current_token() and self.current_token()[0] == 'EXPONENT':
            op = self.consume()[1]
            right = self.factor()
            node = BinaryOpNode(node, op, right)
        return node

    def factor(self):
        """Handle numbers, variables, functions, and parenthesized expressions."""
        token = self.current_token()
        
        if token[0] == 'NUMBER':
            return NumberNode(float(self.consume()[1]))
        elif token[0] == 'VARIABLE':
            return VariableNode(self.consume()[1])
        elif token[0] == 'PI':
            self.consume()
            return NumberNode(math.pi)
        elif token[0] == 'E':
            self.consume()
            return NumberNode(math.e)
        elif token[0] == 'LPAREN':
            self.consume()  # consume '('
            node = self.expression()
            self.consume()  # consume ')'
            return node
        elif token[0] in ['PLUS', 'MINUS']:
            op = self.consume()[1]
            node = self.factor()
            return UnaryOpNode(op, node)
        elif token[0] in ['SIN', 'COS', 'TAN', 'SQRT']:
            return self.function_call()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def function_call(self):
        """Handle functions like sin, cos, tan, sqrt."""
        func_name = self.consume()[1]
        self.consume()
        arg = self.expression()
        self.consume()
        return FunctionCallNode(func_name, [arg])

    def current_token(self):
        """Return the current token, or None if there are no more tokens."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        """Consume and return the current token."""
        token = self.current_token()
        self.pos += 1
        return token
