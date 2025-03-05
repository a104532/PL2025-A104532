import sys
import ply.lex as lex

# Lista de tokens
tokens = [
    'COMMENT',
    'SELECT',
    'WHERE',
    'LIMIT',
    'LBRACE',
    'RBRACE',
    'DOT',
    'COMMA',
    'STRLIT',
    'NUMBER',
    'VARIABLE',
    'PREDICATE',
    'PREFIX'
]


# Regras para tokens
def t_COMMENT(t):
    r'\#.*'
    return t


def t_SELECT(t):
    r'(?i:select)'
    return t


def t_WHERE(t):
    r'(?i:where)'
    return t


def t_LIMIT(t):
    r'(?i:LIMIT)'
    return t


def t_LBRACE(t):
    r'{'
    return t


def t_RBRACE(t):
    r'}'
    return t


def t_DOT(t):
    r'\.'
    return t


def t_COMMA(t):
    r','
    return t


def t_VARIABLE(t):
    r'\?\w+'
    return t


def t_PREFIX(t):
    r'[a-z]+:'
    return t


def t_PREDICATE(t):
    r'a|[A-Za-z]\w*'
    return t

def t_STRLIT(t):
    r'"[^"]*"(?:@\w+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t .lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


if __name__ == '__main__':

    data = sys.stdin.read()

    lexer.input(data)

    for token in lexer:
        print(f"LexToken({token.type},{repr(token.value)},{token.lineno},{token.lexpos})")