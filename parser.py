import math
from math import pi, e
from nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode


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
        while self.current_token()[0] in ['PLUS', 'MINUS']:
            op = self.consume()[1]
            right = self.term()
            node = BinaryOpNode(node, op, right)
        return node

    def term(self):
        """Handle multiplication and division."""
        node = self.factor()
        while self.current_token()[0] in ['TIMES', 'DIVIDE']:
            op = self.consume()[1]
            right = self.factor()
            node = BinaryOpNode(node, op, right)
        return node

    def factor(self):
        """Handle numbers, variables, and parenthesized expressions."""
        token = self.current_token()
        if token[0] == 'NUMBER':
            return NumberNode(float(self.consume()[1]))
        elif token[0] == 'VARIABLE':
            return VariableNode(self.consume()[1])
        elif token[0] == 'LPAREN':
            self.consume()  # consume '('
            node = self.expression()
            self.consume()  # consume ')'
            return node
        elif token[0] in ['SIN', 'COS', 'TAN']:
            return self.function_call()
        elif token[0] == 'PI':
            self.consume()
            return NumberNode(math.pi)
        elif token[0] == 'E':
            self.consume()
            return NumberNode(math.e)
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def function_call(self):
        """Handle functions like sin, cos, tan."""
        func_name = self.consume()[1]
        self.consume()  # consume '('
        arg = self.expression()
        self.consume()  # consume ')'
        return FunctionCallNode(func_name, [arg])

    def current_token(self):
        """Return the current token."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        """Consume and return the current token."""
        token = self.current_token()
        self.pos += 1
        return token

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
    
    def parse(self):
        return self.expression()
    
    def expression(self):
        """
        Parses an expression with addition and subtraction.
        """
        result = self.term()
        while self.current_token() in ('PLUS', 'MINUS'):
            operator = self.current_token()
            self.advance()
            right = self.term()
            if operator == 'PLUS':
                result = ('ADD', result, right)
            elif operator == 'MINUS':
                result = ('SUB', result, right)
        return result
    
    def term(self):
        """
        Parses terms with multiplication and division.
        """
        result = self.factor()
        while self.current_token() in ('TIMES', 'DIVIDE'):
            operator = self.current_token()
            self.advance()
            right = self.factor()
            if operator == 'TIMES':
                result = ('MUL', result, right)
            elif operator == 'DIVIDE':
                result = ('DIV', result, right)
        return result
    
    def factor(self):
        """
        Parses numbers, functions, constants, and parentheses.
        """
        if self.current_token() == 'NUMBER':
            value = self.current_value()
            self.advance()
            return ('NUMBER', value)
        
        elif self.current_token() == 'PI':
            self.advance()
            return ('NUMBER', pi)  # Use the math.pi constant
        
        elif self.current_token() == 'E':
            self.advance()
            return ('NUMBER', e)  # Use the math.e constant
        
        elif self.current_token() == 'SIN':
            self.advance()
            if self.current_token() != 'LPAREN':
                raise SyntaxError("Expected '(' after sin")
            self.advance()
            argument = self.expression()
            if self.current_token() != 'RPAREN':
                raise SyntaxError("Expected ')' after argument of sin")
            self.advance()
            return ('SIN', argument)
        
        elif self.current_token() == 'COS':
            self.advance()
            if self.current_token() != 'LPAREN':
                raise SyntaxError("Expected '(' after cos")
            self.advance()
            argument = self.expression()
            if self.current_token() != 'RPAREN':
                raise SyntaxError("Expected ')' after argument of cos")
            self.advance()
            return ('COS', argument)
        
        elif self.current_token() == 'TAN':
            self.advance()
            if self.current_token() != 'LPAREN':
                raise SyntaxError("Expected '(' after tan")
            self.advance()
            argument = self.expression()
            if self.current_token() != 'RPAREN':
                raise SyntaxError("Expected ')' after argument of tan")
            self.advance()
            return ('TAN', argument)
        
        elif self.current_token() == 'LPAREN':
            self.advance()
            result = self.expression()
            if self.current_token() != 'RPAREN':
                raise SyntaxError("Expected ')'")
            self.advance()
            return result
        
        raise SyntaxError("Invalid syntax")
    
    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position][0]
        return None
    
    def current_value(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position][1]
        return None
    
    def advance(self):
        self.position += 1
