import math
from nodes import NumberNode, VariableNode, BinaryOperationNode, AssignmentNode, PrintNode, FunctionNode

class Interpreter:
    def __init__(self, memory=None):
        self.variables = memory if memory is not None else {}

    def interpret(self, nodes):
        for node in nodes:
            self.evaluate(node)

    def evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, VariableNode):
            if node.name in self.variables:
                return self.variables[node.name]
            elif node.name == "PI":
                return math.pi
            elif node.name == "E":
                return math.e
            else:
                raise ValueError(f"Undefined variable: {node.name}")
        elif isinstance(node, BinaryOperationNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                if right == 0:
                    raise ValueError("Division by zero is not allowed")
                return left / right
            elif node.operator == '**':
                return left ** right
        elif isinstance(node, FunctionNode):
            arguments = [self.evaluate(arg) for arg in node.arguments]
            if hasattr(math, node.function_name):
                return getattr(math, node.function_name)(*arguments)
            else:
                raise ValueError(f"Unsupported function: {node.function_name}")
        elif isinstance(node, AssignmentNode):
            value = self.evaluate(node.value)
            self.variables[node.variable] = value
        elif isinstance(node, PrintNode):
            if node.variable in self.variables:
                print(self.variables[node.variable])
            else:
                raise ValueError(f"Undefined variable: {node.variable}")
