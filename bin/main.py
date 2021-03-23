# -*- coding: utf-8 -*-
import ply.lex as lex 
import ply.yacc as yacc
import sys

ase = open( sys.argv[1]+"s", "a" )
ase.truncate(0)

jampc = 0

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
    "LNAMI",
    "RNAMI",
    "STA",
    "IF1",
    "IF2",
)

t_ignore = ' \t'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'\='
t_LKAKKO = r'\('
t_RKAKKO = r'\)'
t_LNAMI = r'{'
t_RNAMI = r'}'
t_STA    = r"{"
t_IF1    = r">"
t_IF2    = r"<"

def t_NAME(t):
    r"[a-zA-Z0-9&\,]+"
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print (u"不正な文字 '%s'" % t.value[0])


lexer = lex.lex()


def p_mov(p):
    "expr : NAME NAME EQUAL NAME"
    if p[1] == "str":
        ase.write( "mode>str;\n" )
    elif p[1] == "int":
        ase.write( "mode>int;\n" )
    ase.write( "mov "+str( p[2] )+", "+str( p[4] )+";"+"\n" )


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


def p_subandmov(p):
    "expr : NAME NAME EQUAL NAME MINUS NAME"
    ase.write( "mov "+p[2]+", "+ p[4]+";\n"+ "sub "+p[2]+", "+p[6]+";" )


def p_divandmov(p):
    "expr : NAME NAME EQUAL NAME DIVIDE NAME"
    ase.write( "mov "+p[2]+", "+ p[4]+";\n"+ "div "+p[2]+", "+p[6]+";" )


def p_timandmov(p):
    "expr : NAME NAME EQUAL NAME TIMES NAME"
    ase.write( "mov "+p[2]+", "+ p[4]+";\n"+ "tim "+p[2]+", "+p[6]+";" )


def p_sub(p):
    "expr : NAME NAME MINUS SENT"
    p[0] = "sub "+str( p[2] )+", "+str( p[4] )+";"
    ase.write( p[0]+"\n" )


def p_msg(p):
    "expr : NAME NAME"
    if p[1] == "msg":
        ase.write( "msg "+p[2]+";"+"\n" )
    elif p[1] == "return":
        global funcname
        ase.write( "\nret "+funcname+", "+p[2] )


def p_SENT(p):
    "SENT : expr"
    p[0] = p[1]


def p_define(p):
    "expr : NAME NAME LKAKKO NAME RKAKKO LNAMI"
    global funcname
    funcname = p[2]+"("+p[4]+")"
    ase.write( "\n"+funcname+":"+"\n" )
    
    for p in p[4].split( "," ):
        ase.write( "pop "+p+";\n" )


def p_if(p):
    "expr : NAME NAME IF1 NAME LNAMI"
    global jampc
    ase.write( "jnp "+p[2]+", "+p[4]+", L"+str( jampc )+";"+"\n"+"L"+str( jampc )+":"+"\n" )
    jampc+=1

def p_if2(p):
    "expr : NAME NAME IF2 NAME LNAMI"
    global jampc
    ase.write( "ja "+p[2]+", "+p[4]+", L"+str( jampc )+";"+"\n"+"L"+str(jampc)+":"+"\n" )
    jampc+=1


def p_if3(p):
    "expr : NAME NAME EQUAL EQUAL NAME LNAMI"
    global jampc
    ase.write( "jae "+p[2]+", "+p[5]+", L"+str( jampc )+";"+"\n"+"L"+str(jampc)+":"+"\n" )
    jampc+=1


def p_while(p):
    "expr : NAME NAME LNAMI"
    global jampc
    ase.write( "jmp L"+str( jampc )+", "+p[2]+";\n\nL"+str( jampc )+"():\n" )
    jampc+=1


def p_call(p):
    "expr : NAME LKAKKO NAME RKAKKO"
    ase.write( "call "+p[1]+"["+p[3]+"];"+"\n" )


def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]


def p_error(p):
    pass

parser = yacc.yacc()

if __name__ == '__main__':
    file = open( sys.argv[1], "r" )
    data = file.read().split("    ")
    file.close()
    for i in range( len(data) ):
        lexer.input(data[i])
        parser.parse(data[i])
