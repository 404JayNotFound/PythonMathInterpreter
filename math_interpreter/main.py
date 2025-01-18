from math_interpreter.commands.commands import evaluate_expression, handle_variable_assignment, display_help, clear_workspace, list_variables, show_history, exit_interpreter
from math_interpreter.variables import variables
from math_interpreter.core.lexer import validate_input

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
            validate_input(expression)

            command = expression.lower().strip()
            if command in commands:
                commands[command]()
                if command in ['exit', 'quit']:
                    break
                continue

            elif '=' in expression:
                handle_variable_assignment(expression)

            else:
                for var_name in variables:
                    expression = expression.replace(var_name, str(variables[var_name]))
                try:
                    result = evaluate_expression(expression)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Unknown command or invalid expression")
                    print("Type 'help' for a list of available commands.")

        except KeyboardInterrupt:
            print("\nExiting the interpreter. Goodbye!")
            break
        except Exception as e:
            print(f"{e}")

if __name__ == "__main__":
    main()
