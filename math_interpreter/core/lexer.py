import re

allowed_chars = set("0123456789+-*/^()=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. ")

# Token specifications
token_specification = [
    ('NUMBER', r'\d+(\.\d*)?'),
    ('PI', r'pi'),
    ('E', r'e'),
    ('SIN', r'sin'),
    ('COS', r'cos'),
    ('TAN', r'tan'),
    ('ASIN', r'asin'),
    ('ACOS', r'acos'),
    ('ATAN', r'atan'),
    ('SQRT', r'sqrt'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('EXPONENT', r'\^'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('VARIABLE', r'[a-zA-Z]+'),
    ('EOF', r'$'),
]

# Join all token patterns into one regex
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(text):
    """
    Tokenize the input text using the token_specification.
    """
    for mo in re.finditer(token_regex, text):
        kind = mo.lastgroup
        value = mo.group()
  
        if kind == 'NUMBER':
            value = float(value)
        elif kind == 'EOF':
            break
        yield kind, value

def validate_input(expression):
    """Check if the input expression is valid."""
    if any(char not in allowed_chars for char in expression):
        raise ValueError(f"Invalid character in '{expression}'.")
    if expression.count('(') != expression.count(')'):
        raise ValueError(f"Mismatched parentheses in '{expression}'.")