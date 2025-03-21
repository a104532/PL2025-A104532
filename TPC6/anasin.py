import ply.yacc as yacc
from calc_lex import tokens, get_tokens

class Parser:

    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = None
        self.next()

    def next(self):
        "Para precorrer os tokens"
        if self.pos >= len(self.tokens):
            self.current = self.tokens[self.pos]
            self.pos += 1
        else:
            self.current = None

    def match(self, token_type):
        "Verifica o tipo atual do token"
        if self.current and self.current.type == token_type:
            value = self.current.value
            self.next()
            return value
        else:
            raise SyntaxError(f"Esperado token {token_type}, encontrado {self.current}")

    def parse(self):
        return self.expr()

    def expr(self):
        """Regra para expressão: expr -> term { ('+' | '-') term }"""
        result = self.term()

        while self.current and self.current.type in ('ADD', 'SUB'):
            if self.current.type == 'ADD':
                self.match('ADD')
                result += self.term()
            else:
                self.match('SUB')
                result -= self.term()

        return result

    def term(self):
        """Regra para termo: term -> factor { ('*' | '/') factor }"""
        result = self.factor()

        while self.current and self.current.type in ('MUL', 'DIV'):
            if self.current.type == 'MUL':
                self.match('MUL')
                result *= self.factor()
            else:
                self.match('DIV')
                divisor = self.factor()
                if divisor == 0:
                    raise ZeroDivisionError("Divisão por zero")
                result /= divisor

        return result

    def factor(self):
        """Regra para fator: factor -> NUMBER | '(' expr ')' | '-' factor"""
        if self.current.type == 'NUMBER':
            return self.match('NUMBER')
        elif self.current.type == 'AP':
            self.match('AP')
            result = self.expr()
            self.match('FP')
            return result
        elif self.current.type == 'SUB':
            self.match('SUB')
            return -self.factor()
        else:
            raise SyntaxError(f"Token inesperado: {self.current}")

    def evaluate_expression(expression):
        tokens_list = get_tokens(expression)
        parser = Parser(tokens_list)
        result = parser.parse()
        return result

    if __name__ == "__main__":
        test_expressions = [
            "2+3",
            "67-(2+3*4)",
            "(9-2)*(13-4)",
            "5*-2",
            "10/2+3*4"
        ]

        for expr in test_expressions:
            try:
                result = evaluate_expression(expr)
                print(f"Expressão: {expr} = {result}")
            except Exception as e:
                print(f"Erro ao avaliar '{expr}': {e}")
