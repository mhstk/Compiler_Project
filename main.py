from lexer import Lexer

lexer = Lexer().build()
with open('test-cases\\lexer\\test3.txt') as f:
    result = open('output\\lexer\\output3.txt', 'w')
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        result.write(str(tok) + '\n')
