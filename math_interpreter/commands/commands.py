from math_interpreter.core.evaluator import Evaluator
from math_interpreter.core.lexer import tokenize
from math_interpreter.core.parser import Parser
from math_interpreter.variables import variables, history

def evaluate_expression(expression):
    """Tokenize, parse, and evaluate the given mathematical expression."""
    tokens = list(tokenize(expression))
    parser = Parser(tokens)
    ast = parser.parse()
    evaluator = Evaluator()
    result = evaluator.evaluate(ast)
    history.append(f"{expression} = {result}")
    return result

def handle_variable_assignment(expression):
    """Handle assignment of values to variables (e.g., x = 5)."""
    if '=' in expression:
        var_name, expr = expression.split('=', 1)
        var_name = var_name.strip()
        expr = expr.strip()
        result = evaluate_expression(expr)
        variables[var_name] = result
        history.append(f"{var_name} = {result}")
        print(f"{var_name} = {result}")
        return True
    return False

def display_help():
    """Display help message with available commands."""
    print("""
Available Commands:
----------------------
- exit, quit, Ctrl + C    : Exit the interpreter and stop the session.
- <variable> = <expression> : Assign a value to a variable. You can use variables in expressions (e.g., 'x = 5', 'y = x + 2').
- <expression>            : Evaluate a mathematical expression. This could include basic arithmetic, functions (like sin, cos), and constants (like pi, e). Example: '3 + 2 * sin(3)' or 'pi + 2'.
- help                    : Show this list of available commands to guide you through using the interpreter.
- clear                   : Clear the current workspace, including all variables and functions stored in memory.
- list                    : Display all currently defined variables and their values.
- history                 : View a list of previously evaluated expressions in the current session.
    """)

def clear_workspace():
    """Clear all stored variables."""
    global variables
    variables = {}
    print("Workspace cleared. All variables have been removed.")

def list_variables():
    """List all currently defined variables."""
    if variables:
        for var_name, value in variables.items():
            print(f"{var_name} = {value}")
    else:
        print("No variables defined.")

def add_to_history(expression, result):
    """Add an expression and its result to the history."""
    history.append(f"{expression} = {result}")

def show_history():
    """Display all evaluated expressions and their results."""
    if history:
        for entry in history:
            print(entry)
    else:
        print("No history available.")

def exit_interpreter():
    """Exit the interpreter."""
    print("Exiting the interpreter. Goodbye!")
    return False
