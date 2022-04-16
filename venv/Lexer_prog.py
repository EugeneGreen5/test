
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_VAR = 'VAR'
TT_SIGN = 'SIGN'

#Задание алфавита
alphabet = ''
for i in range(97,123):
    alphabet+=chr(i)
for i in range(65,91):
    alphabet+=chr(i)
#Задание алфавита

DIGITS = '0123456789'
VAR = alphabet

class Token:
    def __init__(self,type,value=None):
        self.type = type
        self.value = value
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'
class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def Token(self):
        tokens = []

        while self.current_char != None :
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TT_SIGN))
                self.advance()
            elif self.current_char in VAR:
                tokens.append(self.make_string())
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()

        return tokens
    def make_number(self):
        num_str = ''
        counter = 0
        while self.current_char != None and (self.current_char in DIGITS or self.current_char =='.'):
            if self.current_char == '.':
                if counter == 1: break
                counter += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if counter == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
    def make_string(self):
        string = ''
        counter_str = 0
        while self.current_char != None and self.current_char in VAR:
            string += self.current_char
            self.advance()
        return Token(TT_VAR,string)
def run(text):
    lexer = Lexer(text)
    tokens = lexer.Token()
    return tokens