from sly import Lexer

class MyLexer(Lexer):
    # Set of token names
    tokens = { PLUS , MINUS , MUL , DIVIDE, #binary operators
               DOTADD, DOTSUB, DOTMUL, DOTDIV, #matrix binary operators
               ADDASIGN, SUBASSIGN, MULASSIGN, DIVASSIGN, #assign operators
               LT, GT, LE, GE, NE, EQ, # relational operators
               IF, ELSE, FOR, WHILE, BREAK, CONTINUE, RETURN,
               EYE, ZEROS, ONES, PRINT,
               ID,
               INTNUM,                      #others
               FLOATNUM,
               STRING}
    
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    DOTADD = r'\.\+'
    DOTSUB = r'\.-'
    DOTMUL = r'\.\*'
    DOTDIV = r'\./'
    EQ = r'=='
    ADDASIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN =r'/='
    LE = r'<='
    GE = r'>='
    NE = r'!='
    LT = r'<'
    GT = r'>'
    PLUS = r'\+'
    MINUS = r'-'
    MUL = r'\*'
    DIVIDE = r'/'
    ID['if'] = IF 
    ID['else'] = ELSE 
    ID['for'] = FOR 
    ID['while'] = WHILE
    ID['break'] = BREAK 
    ID['continue'] = CONTINUE 
    ID['return'] = RETURN 
    ID['eye'] = EYE 
    ID['zeros'] = ZEROS 
    ID['ones'] = ONES  
    ID['print'] = PRINT 

    literals = {'=', '(', ')', '{', '}', '[',']', ':' , ',' , ';' , "'" , ':'}

    ignore_tab = r' \t'
    ignore_space = r' '
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    @_(r"[-+]?\d*\.\d+([eE][-+]?\d+)?")
    def FLOATNUM(self, t):
        t.value = float(t.value)
        return t

    @_(r'\b-?\d+\b')
    def INTNUM(self, t):
        t.value = int(t.value)
        return t
    
    @_(r'\"(.*)\"')
    def STRING(self, t):
        t.value = str(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("(%d): Unknown character %r" % (self.lineno, t.value[0]))
        self.index += 1

def main():

    lexer = MyLexer()

    while True:
        print("To end the program input 1\n")
        filename = input("Insert file for scanner: ")

        if filename == "1":
            break

        with open(filename, 'r') as file:
            data = file.read()


        for tok in lexer.tokenize(data):
            print("(" + str(tok.lineno) + "): " + str(tok.type) + "(" + str(tok.value) + ")")
            

if __name__ == "__main__":

    main()








