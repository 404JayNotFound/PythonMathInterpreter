# 🧮 **Python Math Interpreter**  
A modular and extensible Python-based math interpreter capable of parsing and evaluating complex mathematical expressions with precision and clarity.

---

## 📑 **Table of Contents**  
1. [Overview](#overview)  
2. [Features](#features)  
3. [Core Architecture](#core-architecture)  
4. [Lexer](#lexer)  
5. [Parser](#parser)  
6. [Evaluator](#evaluator)  
7. [Setup Instructions](#setup-instructions)  
8. [Testing](#testing)  
9. [Future Enhancements](#future-enhancements)  
10. [Contact](#contact)  

---

## 🧭 **Overview**  
The **Python Math Interpreter** is a robust, modular, and extensible system designed to parse, tokenize, and evaluate mathematical expressions efficiently. This interpreter supports advanced mathematical functions, trigonometry, constants like `pi` and `e`, and workspace management features such as defining and reusing variables.

This project is ideal for applications in scientific computation, automation, and as a foundation for more complex symbolic mathematics engines.

---

## 🌟 **Features**  

- **Core Arithmetic Operations**: Supports addition, subtraction, multiplication, division, and exponentiation.  
- **Constants**: Built-in support for `pi` (3.14159...) and `e` (2.718...).  
- **Trigonometric Functions**: Includes functions such as `sin`, `cos`, `tan`, and their inverses (`asin`, `acos`, `atan`).  
- **Square Root and Exponentiation**: Provides `sqrt` and `^` operators for complex calculations.  
- **Variables**: Easily define, update, and reference variables.  
- **Error Handling**: Comprehensive validation for invalid inputs, undefined variables, and unsupported operations.  

---

## 🛠️ **Core Architecture**  

###  **Workflow Overview**  
1. **Tokenization**: The input expression is converted into tokens via the lexer.  
2. **Parsing**: Tokens are analyzed and structured into an Abstract Syntax Tree (AST).  
3. **Evaluation**: The AST is traversed and executed to compute results.  

###  **Component Breakdown**  

- **Lexer**: Converts input strings into manageable tokens.
- **Parser**: Constructs the AST, ensuring proper precedence and syntax.  
- **Evaluator**: Recursively evaluates the AST for a final result.  
- **Workspace Manager**: Handles variables and commands for efficient workflow management.  

---

## 🔍 **Lexer**  
The lexer scans the input string and produces a sequence of tokens.  

###  **Token Types**  
- **Operators**: `+`, `-`, `*`, `/`, `^`.  
- **Parentheses**: `(`, `)`.  
- **Numbers**: Integer and floating-point values.  
- **Functions**: `sin`, `cos`, `sqrt`, etc.  
- **Variables**: Alphanumeric variable names.  

###  **Error Handling**  
- Detects invalid characters, unexpected symbols, or malformed expressions.  

---

## 🌲 **Parser**  
The parser takes tokens from the lexer and constructs an Abstract Syntax Tree (AST).  

###  **AST Node Types**  
1. **NumberNode**: Represents numeric literals.  
2. **BinaryOpNode**: Handles binary operations like addition or multiplication.  
3. **UnaryOpNode**: Manages unary operations like negation.  
4. **FunctionCallNode**: Executes mathematical functions (`sin`, `cos`, etc.).  

###  **Operator Precedence**  
The parser ensures correct precedence for expressions such as `3 + 4 * 2`, evaluating multiplication before addition.  

---

## 🔄 **Evaluator**  
The evaluator traverses the AST to compute results.  

###  **Evaluation Process**  
- **Binary Operations**: Calculates operations like addition (`+`) or exponentiation (`^`).  
- **Functions**: Executes mathematical functions using Python’s `math` library.  
- **Error Handling**: Raises exceptions for undefined variables or unsupported operations.  

---

## 💻 **Setup Instructions**  

1. **Clone the Repository**:  
   ``` 
   git clone https://github.com/yourusername/PythonMathInterpreter.git
   cd python-math-interpreter
   ```
2. **Ensure you have Python 3.6 or later installed.**
3. **Install dependencies** (if any).
4. **Run the interpreter:**
   
    ```bash
    python main.py
    ```
---

## 🧪 **Testing**
The project includes a comprehensive suite of unit tests for the lexer, parser, and evaluator.

###  **Run Tests**
  Use the following command to execute all tests:
  ```
  python -m unittest discover tests
  ```

###  **Test Coverage**

- **Lexer:** Validates token generation and edge-case handling.
- **Parser:** Ensures correct AST construction and operator precedence.
- **Evaluator:** Tests accurate computation and error reporting.

---

## 🔧 **Future Enhancements**

-  **Advanced Mathematical Functions:** Add support for log, ln, and hyperbolic functions.
-  **Workspace Enhancements:** Introduce functionality for saving and loading variable states.
-  **Performance Optimizations:** Optimize the evaluation process for large and complex expressions.
-  **Visualization:** Include a graphing module for plotting equations and functions.

---

## 💬 Contact
Feel free to explore, or reach out for questions. You can contact me via GitHub or email for inquiries related to any specific project.

## Contributors
- [Jamie O'Connor](https://github.com/404JayNotFound)
