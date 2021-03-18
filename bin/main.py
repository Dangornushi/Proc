# -*- coding: utf-8 -*-
import ply.lex as lex 
import ply.yacc as yacc
import sys

ase = open( sys.argv[1]+"s", "a" )
ase.truncate(0)

# トークンリスト 常に必須
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    "NAME",
    "EQUAL",
    "LKAKKO",
    "RKAKKO",
    "STA",
    "END",
)

# 正規表現による簡単なトークンのルール
t_ignore = ' \t'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'\='
t_LKAKKO = r'\('
t_RKAKKO = r'\)'
t_STA    = r":"
t_END    = r"end"

def t_NAME(t):
    r"[a-z0-9]+"
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# 行番号をたどれるように
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# エラーハンドリングルール
def t_error(t):
    print (u"不正な文字 '%s'" % t.value[0])


# lexer を構築
lexer = lex.lex()


def p_mov(p):
    "expr : NAME NAME EQUAL NAME"
    if p[1] == "str":
        ase.write( "mode>str;\n" )
    elif p[1] == "int":
        ase.write( "mode>int;\n" )
    ase.write( "mov "+str( p[2] )+", "+str( p[4] )+";" )


def p_add(p):
    "expr : NAME NAME PLUS SENT"
    p[0] = "add "+str( p[2] )+", "+str( p[4] )+";"
    ase.write( p[0]+"\n" )


def p_addandmov(p):
    "expr : NAME NAME EQUAL NAME PLUS NAME"
    if p[1] == "str":
        ase.write( "mode>str;\n" )
    elif p[1] == "int":
        ase.write( "mode>int;\n" )
    ase.write( "mov "+p[2]+", "+ p[4]+";\n"+ "add "+p[2]+", "+p[6]+";" )


def p_msg(p):
    "expr : NAME NAME"
    if p[1] == "msg":
        ase.write( "\nmsg "+p[2]+";" )


def p_subandmov(p):
    "expr : NAME NAME EQUAL NAME MINUS NAME"
    if p[1] == "str":
        ase.write( "mode>str;\n" )
    elif p[1] == "int":
        ase.write( "mode>int;\n" )
    ase.write( "mov "+p[2]+", "+ p[4]+";\n"+ "sub "+p[2]+", "+p[6]+";" )


def p_sub(p):
    "expr : NAME NAME MINUS SENT"
    p[0] = "sub "+str( p[2] )+", "+str( p[4] )+";"
    ase.write( p[0]+"\n" )


def p_SENT(p):
    "SENT : expr"
    p[0] = p[1]


def p_define(p):
    "expr : NAME NAME LKAKKO NAME RKAKKO STA"
    ase.write( p[2]+":"+"\n" )


def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]


def p_error(p):
    pass

parser = yacc.yacc()

if __name__ == '__main__':  
    file = open( sys.argv[1], "r" )
    data = file.read().replace( "\n", "" ).split("    ")
    file.close()
    for i in range( len(data) ):
        lexer.input(data[i])
        parser.parse(data[i])
        #print(data[i])
        
        while True:
            tok = lexer.token()
            if not tok:  
                # これ以上トークンはない
                break
