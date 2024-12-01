import re

TOKENS = {
    'KEYWORD_SET': r'\bset\b',
    'KEYWORD_TO': r'\bto\b',
    'KEYWORD_SHOW': r'\bshow\b',
    'IDENTIFIER': r'\b[A-Z][a-zA-Z0-9]*\b',
    'NUMBER': r'\d+(\.\d+)?',
    'OPERATOR': r'(\*\*|[\+\-\*/])',  # Match ** before other operators
    'FUNCTION': r'\b(sin|cos|tan|sqrt|log|exp|asin|acos|atan|ceil|floor|fabs|factorial|pow)\b',  # Function names
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'SEMICOLON': r';',
    'COMMENT': r'\$\$.*',
    'COMMA': r','
}

def lexer(code):
    tokens = []
    pos = 0
    while pos < len(code):
        match = None
        # Skip whitespace
        if code[pos].isspace():
            pos += 1
            continue
        # Match tokens
        for token_type, pattern in TOKENS.items():
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                if token_type != 'COMMENT':  # Ignore comments
                    tokens.append((token_type, match.group()))
                pos = match.end()  # Move to the end of the matched token
                break
        if not match:
            raise ValueError(f"Illegal character at position {pos}: '{code[pos]}'")
    return tokens
