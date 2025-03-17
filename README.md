# 🧮 **Python Math Interpreter**

An interpreter written from scratch in Python, designed to evaluate mathematical expressions. This interpreter provides a hands-on approach to understanding how computers process human-readable text and perform complex calculations. It serves as an excellent introduction to how interpreters and compilers work, which is essential knowledge when developing your own programming language or data language.

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
The **Python Math Interpreter** demonstrates how a computer can transform raw human input (in the form of mathematical expressions) into meaningful output. It breaks down the process into three main stages: tokenization (lexer), parsing (parser), and evaluation (evaluator). These steps mirror the fundamental processes used in programming languages, compilers, and advanced mathematical engines, providing an ideal foundation for learning about how computers interpret data.

---

## 🌟 **Features**  

- **Core Arithmetic Operations**: Supports addition, subtraction, multiplication, division, and exponentiation.  
- **Constants**: Built-in support for mathematical constants like `pi` (3.14159...) and `e` (2.718...).  
- **Trigonometric Functions**: Includes functions like `sin`, `cos`, `tan`, and their inverses (`asin`, `acos`, `atan`).  
- **Square Root and Exponentiation**: Supports `sqrt` and `^` operators for complex calculations.  
- **Variables**: Allows defining, updating, and referencing variables to make calculations reusable.  
- **Error Handling**: Comprehensive checks for invalid inputs, undefined variables, and unsupported operations.  

---

## 🛠️ **Core Architecture**  

### **Workflow Overview**  
1. **Tokenization**: The input string is first converted into a series of tokens by the lexer.  
2. **Parsing**: Tokens are analyzed and arranged into an Abstract Syntax Tree (AST) that represents the structure of the expression.  
3. **Evaluation**: The AST is traversed to perform the calculations and produce the final result.

### **Component Breakdown**  

- **Lexer**: Breaks down the input into tokens, which are the basic units of information.
- **Parser**: Uses the tokens to form a structure, the Abstract Syntax Tree (AST), which dictates the order of operations.
- **Evaluator**: Recursively evaluates the AST to compute the result.
- **Workspace Manager**: Keeps track of variable assignments and the user’s workspace.

---

## 🔍 **Lexer**

The **lexer** is the first step in processing a mathematical expression. It scans the raw input string and breaks it down into "tokens," which are smaller, meaningful pieces. Think of this like how humans break down a sentence into individual words—each token has its own role in the expression, whether it’s a number, an operator, or a function.

### **How the Lexer Works**  
For the input expression `12 + 24`, the lexer identifies the following tokens:  
- `NUMBER:12`  
- `PLUS`  
- `NUMBER:24`  

The lexer’s job is to identify the type of each token, such as numbers, operators (`+`, `-`, `*`, `/`), and functions (`sin`, `cos`, etc.), just like how we identify words as nouns, verbs, and adjectives in a sentence.

Whitespace is usually ignored by the lexer, as it doesn't contribute to the meaning of the expression.

After tokenizing the input, the tokens are passed to the parser for further analysis.

---

## 🌲 **Parser**

The **parser** takes the sequence of tokens and uses them to build a hierarchical structure known as the **Abstract Syntax Tree (AST)**. This tree visually represents the relationships between the tokens, just like how a sentence is parsed to understand its meaning and structure. The parser ensures that the mathematical expression follows the correct order of operations.

### **How the Parser Works**  
In the case of the input `12 + 24`, the parser sees:
- `NUMBER:12`, followed by
- `PLUS`, followed by
- `NUMBER:24`.

The parser understands that the two numbers (`12` and `24`) should be added together. However, if a multiplication operator was present, such as `2 * 3 + 5`, the parser knows to multiply `2` and `3` first (due to operator precedence) before adding `5` to the result.

The parser constructs an AST where each operation and operand is represented as a node. For instance, a simple addition operation would look like this in an AST:

This AST is then passed to the evaluator for execution.

---

## 🔄 **Evaluator**

The **evaluator** traverses the AST and executes the operations as described by the structure of the tree. The evaluator can be thought of as the **“executor”** of the program—the component that performs the actual calculations.

### **How the Evaluator Works**  
The evaluator starts at the root of the AST and works its way down, performing the operations in the correct order. For a simple addition, the evaluator will:

1. Look at the root of the tree (`+` operator).
2. Evaluate the left child (`12`).
3. Evaluate the right child (`24`).
4. Perform the operation: `12 + 24 = 36`.

If the tree contains more complex operations, like multiplication and division, the evaluator ensures those operations are handled first, according to the proper precedence.

The evaluator makes use of Python's built-in `math` library for functions like `sin`, `cos`, and `sqrt`, ensuring accurate computation of mathematical expressions.

---

## 💻 **Setup Instructions**

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/404JayNotFound/PythonMathInterpreter.git
   cd math-interpreter
   ```
2. **Ensure you have Python 3.6 or later installed**.
3. **Install dependencies (if any)**.
4. **Run the interpreter**:
   ```bash
   python main.py
   ```
---

## 🧪 Testing
The project includes a comprehensive suite of unit tests for the lexer, parser, and evaluator.
```bash
python -m unittest discover tests
```

## Test Coverage
- Lexer: Validates correct token generation and edge-case handling.
- Parser: Ensures the AST is correctly built and operator precedence is respected.
- Evaluator: Verifies that calculations are accurate and errors are properly handled.

---

## 🔧 Future Enhancements
- Advanced Mathematical Functions: Add support for more complex functions like logarithms, hyperbolic functions, and advanced constants.
- Workspace Enhancements: Introduce features for saving and loading variable states, creating more complex user workspaces.
- Performance Optimizations: Improve performance for handling larger expressions with deep recursion or complex operations.
- Visualization: Add functionality for graphing mathematical functions to visualize equations in a more interactive manner.

## 💬 Contact
Feel free to explore, or reach out for questions. You can contact me via GitHub or email for inquiries related to any specific project. 

## Contributors
- [Jamie O'Connor](https://github.com/404JayNotFound)
