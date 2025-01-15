from math_interpreter.commands.commands import evaluate_expression, handle_variable_assignment, display_help, clear_workspace, list_variables, show_history, exit_interpreter
from math_interpreter.variables import variables

def main():
    """Main function to run the math interpreter."""
    print("Welcome to the Math Interpreter!")
    print("Type 'help' for a list of available commands.")

    commands = {
        'help': display_help,
        'exit': exit_interpreter,
        'quit': exit_interpreter,
        'clear': clear_workspace,
        'list': list_variables,
        'history': show_history
    }

    while True:
        try:
            expression = input("\nEnter expression: ")
            if expression.lower() in commands:
                commands[expression.lower()]()
            elif '=' in expression:
                handle_variable_assignment(expression)
            else:
                for var_name in variables:
                    expression = expression.replace(var_name, str(variables[var_name]))

                result = evaluate_expression(expression)
                print(f"Result: {result}")

        except KeyboardInterrupt:
            print("\nExiting the interpreter. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
