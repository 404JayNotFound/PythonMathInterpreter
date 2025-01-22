import re

disallowed_chars = set("!@#$%&[]{}|\\,<>?;:'\"`~")

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
    ('WHITESPACE', r'\s+'),
    ('EOF', r'$'),
]

# Join all token patterns into one regex
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(text):
    """
    Tokenize the input text using the token_specification.
    """
    for match in re.finditer(token_regex, text):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NUMBER':
            value = float(value)

        if kind == 'WHITESPACE':
            continue

        if kind == 'EOF':
            break

        yield kind, value

def validate_input(expression):
    """Check if the input expression is valid."""
    if any(char in disallowed_chars for char in expression):
        raise ValueError(f"Invalid character in '{expression}'.")
    
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                raise ValueError(f"Unmatched closing parenthesis in '{expression}'.")
            stack.pop()

    if stack:
        raise ValueError(f"Unmatched opening parenthesis in '{expression}'.")