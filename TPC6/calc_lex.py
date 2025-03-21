import ply.lex as lex

tokens = (
    "NUMBER", # e.g. : 5
    "ADD", # +
    "SUB", # -
    "MUL", # *
    "DIV", # /
    "AP", # (
    "FP" # )
)

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ADD = r"\+"
t_SUB = r"-"
t_MUL = r"\*"
t_DIV = r"/"
t_AP = r"\("
t_FP = r"\)"

t_ignore = " \n" # string -> conjunto de caracteres

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.value = ""
    return t

def t_error(t):
    print(f"Simbolo invalido na linha {t.lineno}: {t.value}")
    t.lexer.skip(1)
    pass

lexer = lex.lex()

def get_tokens(expression):
    lexer.input(expression)
    tokens_list = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens_list.append(token)
    return tokens_list

# Para teste individual deste módulo
if __name__ == "__main__":
    test_expr = "3*(5+2)"
    lexer.input(test_expr)
    print(f"Tokens para '{test_expr}':")
    while token := lexer.token():
        print(token)