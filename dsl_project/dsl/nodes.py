class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode({self.value})"

class VariableNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VariableNode({self.name})"

class BinaryOperationNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOperationNode({self.left}, {self.operator}, {self.right})"

class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return f"AssignmentNode({self.variable}, {self.value})"

class PrintNode:
    def __init__(self, variable):
        self.variable = variable

    def __repr__(self):
        return f"PrintNode({self.variable})"

class FunctionNode:
    def __init__(self, function_name, arguments):
        self.function_name = function_name
        self.arguments = arguments  # List of arguments for multi-arg functions

    def __repr__(self):
        return f"FunctionNode({self.function_name}, {self.arguments})"
