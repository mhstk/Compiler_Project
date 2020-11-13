from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        "program : declist MAIN LRB RRB block"
        print("program : declist MAIN LRB RRB block")

    def p_error(self,  p):
        print("SYNTAX ERROR : " + p.value)
        raise Exception('ParsingError: invalid grammar at ', p)


    def build(self, **kwargs):
        """build the parser"""
        self.parse = yacc.yacc(module=self, **kwargs)
        return self.parse
