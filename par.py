from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def print_args(self, p):
        string = ''
        for i in p:
            string += str(i) + ' '
        return string

    def p_program(self, p):
        'program : declist MAIN LRB RRB block'
        print('program : declist MAIN LRB RRB block')

    def p_declist(self, p):
        'declist : dec'
        '        | declist dec'
        '        | '
        print(f'declist and len is {len(p)}')

    def p_dec(self, p):
        '''dec : vardec 
               | funcdec'''
        print(f'dec and len is {len(p)}')

    def p_type(self, p):
        '''type : INTEGER
                | FLOAT
                | BOOLEAN'''
        print(f'type and len is {len(p)}')

    def p_iddec(self, p):
        '''iddec : ID
                 | ID LSB exp RSB
                 | ID ASSIGN exp'''

        if len(p) == 2:
            print('iddec : ID')
        elif len(p) == 5:
            print('iddec : ID LSB exp RSB')
        else:
            print('iddec : ID ASSIGN exp')

    def p_idlist(self, p):
        '''idlist : iddec 
                  | idlist COMMA iddec'''
        if len(p) == 2:
            print('idlist : iddec')
        else:
            print('idlist : idlist COMMA iddec')

    def p_vardec(self, p):
        '''vardec : idlist COLON type SEMICOLON'''
        print('vardec : idlist COLON type SEMICOLON')

    def p_funcdec(self, p):
        '''funcdec : FUNCTION LRB paramdecs RRB SEMICOLON type block 
                   | FUNCTION ID LRB paramdecs RRB block'''
        if len(p) == 8:
            print('funcdec : FUNCTION LRB paramdecs RRB SEMICOLON type block')
        else:
            print('funcdec : FUNCTION ID LRB paramdecs RRB block')

    def p_paramdecs(self, p):
        '''paramdecs : paramdecslist
                     | '''
        if len(p) == 2:
            print('paramdecs : paramdecslist')
        else:
            print('paramdecs : ')

    def p_paramdecslist(self, p):
        '''paramdecslist : paramdec
                         | paramdecslist COMMA paramdec'''
        if len(p) == 2:
            print('paramdecslist : paramdec')
        else:
            print('paramdecslist : paramdecslist COMMA paramdec')

    def p_paramdec(self, p):
        '''paramdec : ID SEMICOLON type 
                    | ID LSB RSB COLON type'''
        if len(p) == 4:
            print('paramdec : ID SEMICOLON type')
        else:
            print('paramdec : ID LSB RSB COLON type')

    def p_block(self, p):
        '''block : LCB stmtlist RCB'''
        print('block : LCB stmtlist RCB')

    def p_stmtlist(self, p):
        '''stmtlist : stmt
                    | stmtlist stmt
                    | '''
        if len(p) == 2:
            print('stmtlist : stmt')
        elif len(p) == 3:
            print('stmtlist : stmtlist stmt')
        else:
            print('stmtlist : ')

    def p_lvalue(self, p):
        '''lvalue : ID 
                  | ID LSB exp RSB'''
        if len(p) == 2:
            print('lvalue : ID')
        else:
            print('lvalue : ID LSB exp RSB')

    def p_case(self, p):
        '''case : WHERE const COLON stmtlist'''
        print('case : WHERE const COLON stmtlist')

    def p_cases(self, p):
        '''cases : case
                 | cases case
                 | '''
        if len(p) == 2:
            print('cases : case')
        elif len(p) == 3:
            print('cases : cases case')
        else:
            print('cases : ')

    def p_stmt(self, p):
        '''stmt : RETURN exp SEMICOLON 
                | exp SEMICOLON
                | block
                | vardec
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt 
                | FOR LRB ID IN ID RRB stmt
                | IF LRB exp RRB stmt elseiflist 
                | IF LRB exp RRB stmt elseiflist ELSE stmt
                | PRINT LRB ID RRB SEMICOLON'''
        print(f'stmt : {len(p)}')

    def p_elseiflist(self, p):
        '''elseiflist : ELSEIF LRB exp RRB stmt 
                      | elseiflist ELSEIF LRB exp RRB stmt
                      | '''
        if len(p) == 6:
            print('elseiflist : ELSEIF LRB exp RRB stmt')
        elif len(p) == 7:
            print('elseiflist : elseiflist ELSEIF LRB exp RRB stmt')
        else:
            print('elseiflist : ')

    def p_relopexp(self, p):
        '''relopexp : exp relop exp 
                    | relopexp relop exp'''
        if len(p) == 4:
            print('relopexp : exp relop exp')
        else:
            print('relopexp : relopexp relop exp')

    def p_exp(self, p):
        '''exp : lvalue ASSIGN exp 
               | exp operator exp
               | relopexp
               | const
               | lvalue 
               | ID LRB explist RRB 
               | LRB exp RRB
               | ID LRB RRB 
               | SUB exp 
               | NOT exp'''
        print(f'exp : {len(p)}')

    def p_operator(self, p):
        '''operator : AND 
                    | OR
                    | SUM
                    | SUB
                    | MUL
                    | DIV
                    | MOD'''
        print(f'operator : {p.slice[1].type}')

    def p_const(self, p):
        '''const : INTEGERNUMBER 
                 | FLOATNUMBER
                 | TRUE
                 | FALSE'''
        print(f'const : {p.slice[1].type}')

    def p_relop(self, p):
        '''relop : GT 
                 | LT
                 | NE
                 | EQ
                 | LE
                 | GE'''
        print(f'relop : {p.slice[1].type}')

    def p_explist(self, p):
        '''explist : exp 
                   | explist COMMA exp'''
        if len(p) == 2:
            print('explist : exp')
        else:
            print('explist : explist COMMA exp')

    def p_error(self,  p):
        print("SYNTAX ERROR : " + p.value)
        # raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parse = yacc.yacc(module=self, **kwargs)
        return self.parse
