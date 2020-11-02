from lexer import Lexer

lexer = Lexer().build()
with open('test-cases\\lexer\\test1.txt') as f:
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
