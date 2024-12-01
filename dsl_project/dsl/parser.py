from nodes import NumberNode, VariableNode, BinaryOperationNode, AssignmentNode, PrintNode, FunctionNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, token_type):
        if self.current_token() and self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise ValueError(f"Expected {token_type}, got {self.current_token()}")

    def parse(self):
        nodes = []
        while self.current_token():
            nodes.append(self.statement())
        return nodes

    def statement(self):
        token = self.current_token()
        if token[0] == 'KEYWORD_SET':
            return self.assignment()
        elif token[0] == 'KEYWORD_SHOW':
            return self.print_statement()
        else:
            raise ValueError(f"Unexpected token {token}")

    def assignment(self):
        self.consume('KEYWORD_SET')
        variable = self.current_token()[1]
        self.consume('IDENTIFIER')
        self.consume('KEYWORD_TO')
        value = self.expression()
        self.consume('SEMICOLON')
        return AssignmentNode(variable, value)

    def print_statement(self):
        self.consume('KEYWORD_SHOW')
        variable = self.current_token()[1]
        self.consume('IDENTIFIER')
        self.consume('SEMICOLON')
        return PrintNode(variable)

    def expression(self):
        return self.additive()

    def additive(self):
        left = self.multiplicative()
        while self.current_token() and self.current_token()[1] in ('+', '-'):
            operator = self.current_token()[1]
            self.consume('OPERATOR')
            right = self.multiplicative()
            left = BinaryOperationNode(left, operator, right)
        return left

    def multiplicative(self):
        left = self.exponentiation()
        while self.current_token() and self.current_token()[1] in ('*', '/'):
            operator = self.current_token()[1]
            self.consume('OPERATOR')
            right = self.exponentiation()
            left = BinaryOperationNode(left, operator, right)
        return left

    def exponentiation(self):
        left = self.term()
        while self.current_token() and self.current_token()[1] == '**':
            operator = self.current_token()[1]
            self.consume('OPERATOR')
            right = self.term()
            left = BinaryOperationNode(left, operator, right)
        return left

    def term(self):
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return NumberNode(float(token[1]))
        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return VariableNode(token[1])
        elif token[0] == 'FUNCTION':  # Recognize functions like sin, cos, sqrt
            function_name = token[1]
            self.consume('FUNCTION')
            self.consume('LPAREN')
            arguments = []
            while True:
                arguments.append(self.expression())
                if self.current_token()[0] == 'RPAREN':
                    break
                self.consume('COMMA')  # Handle comma-separated arguments
            self.consume('RPAREN')
            return FunctionNode(function_name, arguments)
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            expr = self.expression()
            self.consume('RPAREN')
            return expr
        else:
            raise ValueError(f"Unexpected token {token}")
