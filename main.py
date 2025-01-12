import os
import json
from lexer import tokenize
from parser import Parser
from evaluator import Evaluator

STORAGE_FILE = 'variables.json'

variables = {}

def load_variables():
    """Load saved variables from the JSON file."""
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_variables():
    """Save variables to a JSON file."""
    with open(STORAGE_FILE, 'w') as f:
        json.dump(variables, f)

def evaluate_expression(expression):
    """Tokenize, parse, and evaluate the given mathematical expression."""
    tokens = list(tokenize(expression))
    parser = Parser(tokens)
    ast = parser.parse()
    evaluator = Evaluator()
    return evaluator.evaluate(ast)

def handle_variable_assignment(expression):
    """Handle assignment of values to variables (e.g., x = 5)."""
    if '=' in expression:
        var_name, expr = expression.split('=', 1)
        var_name = var_name.strip()
        expr = expr.strip()

        result = evaluate_expression(expr)
        variables[var_name] = result
        print(f"{var_name} = {result}")
        return True
    return False

def display_help():
    """Display help message with available commands."""
    print("""
Available Commands:
-------------------
- help        : Show this help message.
- exit, quit  : Exit the interpreter.
- <variable> = <expression> : Assign value to a variable.
- <expression> : Evaluate a mathematical expression.
- Ctrl + C     : Exit the interpreter.
    """)

def main():
    """Main function to run the math interpreter."""
    global variables

    print("Welcome to the Math Interpreter!")
    print("Type 'help' for a list of available commands.")

    variables = load_variables()

    while True:
        try:

            expression = input("\nEnter expression: ")

            if expression.lower() == 'help':
                display_help()
                continue

            if expression.lower() in ['exit', 'quit', 'Ctrl + C']:
                save_variables()
                print("Exiting the interpreter. Goodbye!")
                break

            if '=' in expression:
                handle_variable_assignment(expression)
            else:
                for var_name in variables:
                    expression = expression.replace(var_name, str(variables[var_name]))

                result = evaluate_expression(expression)
                print(f"Result: {result}")

        except KeyboardInterrupt:
            print("\nExiting the interpreter. Goodbye!")
            save_variables()
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
