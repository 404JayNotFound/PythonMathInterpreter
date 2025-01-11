class Evaluator:
    def evaluate(self, node):
        if node[0] == 'NUMBER':
            return node[1]
        
        elif node[0] == 'ADD':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left + right
        
        elif node[0] == 'SUB':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left - right
        
        elif node[0] == 'MUL':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            return left * right
        
        elif node[0] == 'DIV':
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        
        raise ValueError("Invalid node type: " + node[0])