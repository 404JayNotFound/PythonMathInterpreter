import re

# Define token types and their regex patterns
token_specification = [
    ('NUMBER', r'\d+(\.\d*)?'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('EOF', r'$'),
]
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(text):
    """
    Tokenizes the input text into a sequence of tokens using regular expressions.
    """
    for mo in re.finditer(token_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = float(value)
        elif kind == 'EOF':
            break
        yield kind, value
