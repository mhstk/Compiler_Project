from lexer import Lexer
from par import Parser

lexer = Lexer().build()
with open('test-cases\\parser\\test1.txt') as f:
    text_input = f.read()
    lexer.input(text_input)
    parser = Parser()
    parser.build().parse(text_input, lexer, False)
