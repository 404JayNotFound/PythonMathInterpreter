import json
import os
from main import evaluate_expression, handle_variable_assignment


# File to store the variables
storage_file = 'variables.json'

def load_variables():
    """
    Load saved variables from a JSON file.
    """
    if os.path.exists(storage_file):
        with open(storage_file, 'r') as f:
            return json.load(f)
    return {}

def save_variables():
    """
    Save the variables to a JSON file.
    """
    with open(storage_file, 'w') as f:
        json.dump(variables, f)

# Load the variables when the program starts
variables = load_variables()

def main():
    print("Welcome to the Math Interpreter!")
    print("Type 'exit' or 'quit' to exit.")
    print("You can define variables by using the syntax: variable = expression")
    
    while True:
        try:
            # Get user input
            expression = input("Expression: ")
            
            if expression.lower() in ['exit', 'quit']:
                # Save variables before exiting
                save_variables()
                print("Goodbye!")
                break
            
            # Check for variable assignment first
            if '=' in expression:
                handle_variable_assignment(expression)
            else:
                # Check if the expression involves variables
                for var_name in variables:
                    expression = expression.replace(var_name, str(variables[var_name]))
                
                # Evaluate the expression
                result = evaluate_expression(expression)
                print(f"Result: {result}")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
