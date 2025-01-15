import re

token_specification = [
    ('NUMBER', r'\d+(\.\d*)?'),
    ('PI', r'pi'),
    ('E', r'e'),
    ('SIN', r'sin'),
    ('COS', r'cos'),
    ('TAN', r'tan'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('EXPONENT', r'\^'),
    ('SQRT', r'sqrt'),
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
