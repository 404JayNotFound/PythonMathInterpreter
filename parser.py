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
        Parses numbers and parentheses.
        """
        if self.current_token() == 'NUMBER':
            value = self.current_value()
            self.advance()
            return ('NUMBER', value)
        
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
