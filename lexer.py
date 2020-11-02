# ------------------------------------------------------------
# lexer.py
#
# tokenizer for a simple expression evaluator for
# tokens in lexer.pdf
# ------------------------------------------------------------

from ply import lex


class Lexer:

    '''
    PLY DOC:
    To handle reserved words, you should write a single rule to match an identifier and do a special name lookup in a function like this:
    reserved = {
        'if' : 'IF',
        'then' : 'THEN',
        'else' : 'ELSE',
        'while' : 'WHILE',
        ...
    }

    tokens = ['LPAREN','RPAREN',...,'ID'] + list(reserved.values())

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'ID')    # Check for reserved words
        return t
    '''

    reserved = {
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN',
        'fun': 'FUNCTION',
        'True': 'TRUE',
        'False': 'FALSE',
        'print': 'PRINT',
        'return': 'RETURN',
        'main': 'MAIN',
        'if': 'IF',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        'while': 'WHILE',
        'on': 'ON',
        'where': 'WHERE',
        'for': 'FOR',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN'
    }

    # List of token names.   This is always required
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER',
        'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV', 'MOD',
        'GT', 'GE', 'LT', 'LE', 'EQ', 'NE',
        'LCB', 'RCB', 'LRB', 'RRB', 'LCB', 'RSB',
        'SEMICOLON', 'COLON', 'COMMA', 'ERROR!'
    ] + list(reserved.values())

    '''
    Docs of ply:
    When building the master regular expression, rules are added in the following order:

    All tokens defined by functions are added in the same order as they appear in the lexer file.
    Tokens defined by strings are added next by sorting them in order of decreasing regular expression length (longer expressions are added first).
    Without this ordering, it can be difficult to correctly match certain types of tokens. For example, if you wanted to have separate tokens for "=" and "==", you need to make sure that "==" is checked first. By sorting regular expressions in order of decreasing length, this problem is solved for rules defined as strings. For functions, the order can be explicitly controlled since rules appearing first are checked first.    
    '''
