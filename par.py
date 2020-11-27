from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    precedence = (
        ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'COLON', 'SEMICOLON'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'GE', 'LT', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'NOT'),
        ('left', 'IF_NOT_ELSE'),
        ('left', 'ELSE', 'ELSEIF'),
    )

    def print_rule(self, p):

        for i, _ in enumerate(p):
            if i == 0:
                print(f'{p.slice[i].type} : ', end='')
            else:
                print(f'{p.slice[i].type}' , end=' ')
        print()

    def __init__(self):
        pass

    def p_program(self, p):
        'program : declist MAIN LRB RRB block'
        self.print_rule(p)

    def p_declist(self, p):
        '''declist : declist dec
                | '''
        self.print_rule(p)
   
    def p_dec(self, p):
        '''dec : vardec 
               | funcdec'''
        self.print_rule(p)
   
    def p_type(self, p):
        '''type : INTEGER
                | FLOAT
                | BOOLEAN'''
        self.print_rule(p)

    def p_iddec(self, p):
        '''iddec : ID
                 | ID LSB exp RSB
                 | ID ASSIGN exp'''
        self.print_rule(p)

    def p_idlist(self, p):
        '''idlist : iddec 
                  | idlist COMMA iddec'''
        self.print_rule(p)

    def p_vardec(self, p):
        '''vardec : idlist COLON type SEMICOLON'''
        self.print_rule(p)

    def p_funcdec(self, p):
        '''funcdec : FUNCTION ID LRB paramdecs RRB COLON type block 
                   | FUNCTION ID LRB paramdecs RRB block'''
        self.print_rule(p)

    def p_paramdecs(self, p):
        '''paramdecs : paramdecslist
                     | '''
        self.print_rule(p)

    def p_paramdecslist(self, p):
        '''paramdecslist : paramdec
                         | paramdecslist COMMA paramdec'''
        self.print_rule(p)
        
    def p_paramdec(self, p):
        '''paramdec : ID COLON type 
                    | ID LSB RSB COLON type'''
        self.print_rule(p)
        
    def p_block(self, p):
        '''block : LCB stmtlist RCB'''
        self.print_rule(p)
        
    def p_stmtlist(self, p):
        '''stmtlist : stmtlist stmt
                    | '''
        self.print_rule(p)
        
    def p_case(self, p):
        '''case : WHERE const COLON stmtlist'''
        self.print_rule(p)

    def p_cases(self, p):
        '''cases : cases case
                 | '''
        self.print_rule(p)

    def p_stmt(self, p):
        '''stmt : RETURN exp SEMICOLON 
                | exp SEMICOLON
                | block
                | vardec
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt 
                | FOR LRB ID IN ID RRB stmt
                | IF LRB exp RRB stmt elseiflist %prec IF_NOT_ELSE
                | IF LRB exp RRB stmt elseiflist ELSE stmt
                | PRINT LRB ID RRB SEMICOLON'''
        self.print_rule(p)

    def p_elseiflist(self, p):
        '''elseiflist : elseiflist ELSEIF LRB exp RRB stmt
                      | '''
        self.print_rule(p)
  
    ## need to merge p_relop and p_relopexp and p_exp 
    def p_exp(self, p):
        '''exp  : ID ASSIGN exp 
                | ID LSB exp RSB ASSIGN exp 
                | exp AND exp
                | exp OR exp
                | exp SUM exp
                | exp SUB exp
                | exp DIV exp
                | exp MUL exp
                | exp MOD exp
                | exp GT exp 
                | exp LT exp
                | exp NE exp
                | exp EQ exp
                | exp LE exp
                | exp GE exp
                | const
                | ID LSB exp RSB 
                | ID  
                | ID LRB explist RRB 
                | LRB exp RRB
                | ID LRB RRB 
                | SUB exp 
                | NOT exp'''
        self.print_rule(p)

    def p_const(self, p):
        '''const : INTEGERNUMBER 
                 | FLOATNUMBER
                 | TRUE
                 | FALSE'''
        self.print_rule(p)

    def p_explist(self, p):
        '''explist : exp 
                   | explist COMMA exp'''
        self.print_rule(p)

    def p_error(self,  p):
        print("SYNTAX ERROR : " + p.value)
        self.print_rule(p)

    def build(self, **kwargs):
        """build the parser"""
        self.parse = yacc.yacc(module=self, **kwargs)
        return self.parse
