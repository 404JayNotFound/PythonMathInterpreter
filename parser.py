from math import pi, e
from nodes import NumberNode, BinaryOpNode, VariableNode, FunctionCallNode


class Parser:
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
