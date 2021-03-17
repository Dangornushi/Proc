from ply import lex
import ply.yacc as yacc
import sys

valldick = {}

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'NAME',
    'EQUAL',
    'MOLD',
)

t_ignore = ' \t'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL   = r"\="

def t_NAME( t ) :
    r'[a-zA-Z]+[a-zA-Z0-9]*'
    return t

def t_MOLD( t ) :
    r"int"
    return t

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
    r'\n+'
    t.lexer.lineno += len( t.value )

def t_error( t ):
    print("Invalid Token:",t.value[0])
    t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)


def p_exprtonum( p ) :
    """ 
    expr : MOLD NAME EQUAL NUMBER
    """
    p[1] = valldick[p[1]]


def p_add( p ) :
    'expr : MOLD expr PLUS expr'
    p[0] = p[1] + p[3]


def p_sub( p ) :
    'expr : MOLD expr MINUS expr'
    p[0] = p[1] - p[3]


def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]


def p_mult_div( p ) :
    '''
    expr    : MOLD expr TIMES expr
            | MOLD expr DIV expr
    '''

    if p[3] == '*' :
        p[2] = p[2] * p[4]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

def p_expr2NAME( p ) :
    "expr : NAME"
    p[0] = p[1]

def p_expr2MOLD( p ) :
    "expr : MOLD"
    p[0] = p[1]

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]


def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]


def p_error( p ):
    pass

parser = yacc.yacc()

def main():
    ase = open( sys.argv[1].split(".")[0]+".prs", "a" )
    ase.truncate(0)
    f = open(sys.argv[1], 'r')
    data = f.read()
    f.close()

    count = 1
    count2 = 0
    retcount = 0


    while True:
        res = parser.parse(data) # the input
        print(res)
        tok = lexer.token()
        if not tok: 
            break

        if tok.type == "FUNCNAME":
            ase.write(tok.value.replace("fn ", "")+":")
        
        elif tok.value == "return":
            count = 0
            retcount = 1

        elif tok.type == "NAME" or tok.type == "EQUAL" or tok.type == "PULS" or tok.type == "NUMBER":
            if count == 1 and retcount == 0:
                if tok.value == "int":
                    ase.write("\nmode>int;")
        
                elif tok.value == "put":
                    count2 = 4
                
                elif tok.value == "str":
                    ase.write("\nmode>str;")
                
                elif tok.type == "NAME" and count2 != 2:
                    arg = tok.value

                elif tok.type == "EQUAL":
                    count2 = 2
                
                elif tok.type == "PULS":
                    count2 = 3

                elif count2 == 2:
                    ase.write("\nmov "+arg+", "+tok.value+";")
                    count = 0
                

                elif count2 == 3:
                    ase.write("\nadd "+arg+", "+tok.value+";")
                    count = 0
                
            elif count2 == 4:
                ase.write("\nput "+arg+";")

        elif tok.type == "SEMI":
            count = 1
    
    ase.close()


if __name__ == '__main__':
    main()