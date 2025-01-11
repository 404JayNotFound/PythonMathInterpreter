from lexer import tokenize
from parser import Parser
from evaluator import Evaluator

def main():
    print("Simple Math Interpreter")
    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == "exit":
                break

            tokens = list(tokenize(expression))

            parser = Parser(tokens)
            ast = parser.parse()

            evaluator = Evaluator()
            result = evaluator.evaluate(ast)
            print(f"Result: {result}")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()