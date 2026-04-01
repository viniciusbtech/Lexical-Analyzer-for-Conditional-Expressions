import sys

class Token:
    def __init__(self, name, attribute=None):
        self.name = name
        self.attribute = attribute

    def __repr__(self):
        attr_display = self.attribute if self.attribute is not None else "None"
        return f"<{self.name}, {attr_display}>"

class RelopToken(Token):
    def __init__(self, op):
        super().__init__("RELOP", op)

class IDToken(Token):
    def __init__(self, lexeme):
        super().__init__("ID", lexeme)

class NumberToken(Token):
    def __init__(self, value):
        super().__init__("NUMBER", value)

class ReservedWordToken(Token):
    def __init__(self, name):
        super().__init__(name.upper(), "None")

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.pos = 0
        self.keywords = {"if", "then", "else"}

    def next_char(self):
        if self.pos < len(self.source):
            char = self.source[self.pos]
            self.pos += 1
            return char
        return None

    def peek_char(self):
        if self.pos < len(self.source):
            return self.source[self.pos]
        return None

    def get_next_token(self):
        while True:
            char = self.next_char()

            if char is None:
                return Token("EOF")

            # --- WHITESPACE (ws → (blank | tab | newline)+ ) ---
            if char.isspace():
                continue

            # --- RELOP ---
            if char == '<':
                next_c = self.peek_char()
                if next_c == '=':
                    self.next_char()
                    return RelopToken("LE")
                elif next_c == '>':
                    self.next_char()
                    return RelopToken("NE")
                else:
                    return RelopToken("LT")

            if char == '>':
                next_c = self.peek_char()
                if next_c == '=':
                    self.next_char()
                    return RelopToken("GE")
                else:
                    return RelopToken("GT")

            if char == '=':
                return RelopToken("EQ")

            # --- IDENTIFICADORES / PALAVRAS RESERVADAS ---
            if char.isalpha():
                lexeme = char
                while self.peek_char() and self.peek_char().isalnum():
                    lexeme += self.next_char()

                if lexeme in self.keywords:
                    return ReservedWordToken(lexeme)
                return IDToken(lexeme)

            # --- NÚMEROS ---
            if char.isdigit():
                lexeme = char

                # parte inteira
                while self.peek_char() and self.peek_char().isdigit():
                    lexeme += self.next_char()

                # parte fracionária
                if self.peek_char() == '.':
                    lexeme += self.next_char()
                    while self.peek_char() and self.peek_char().isdigit():
                        lexeme += self.next_char()

                # exponencial
                if self.peek_char() and self.peek_char().lower() == 'e':
                    lexeme += self.next_char()
                    if self.peek_char() in ['+', '-']:
                        lexeme += self.next_char()

                    if not self.peek_char() or not self.peek_char().isdigit():
                        raise Exception("Erro léxico: expoente inválido")

                    while self.peek_char() and self.peek_char().isdigit():
                        lexeme += self.next_char()

                return NumberToken(float(lexeme))

            # --- ERRO LÉXICO ---
            raise Exception(f"Erro léxico: caractere inesperado '{char}'")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_de_entrada>")
        return

    try:
        with open(sys.argv[1], 'r') as f:
            code = f.read()

        lexer = Lexer(code)

        while True:
            token = lexer.get_next_token()
            print(token)
            if token.name == "EOF":
                break

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()# Lexer para Sentenças Condicionais