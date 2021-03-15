# -*- encoding: utf-8 -*-

import ply.lex as lex
import sys


tokens = (
    "FUNCNAME",
    "MOLDINT",
    'NAME',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'SEMI',
    "LBRACKET",
    "RBRACKET",
    "PULS",
    "MINUS",
    "KAKE",
    "WARU",
    "EQUAL",
)

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}

def t_FUNCNAME(t):
    r"^fn[^fna-zA-Z][a-zA-Z0-9]*"
    return t

t_NAME = '[a-zA-Z\"][a-zA-Z0-9\"]*'
t_NUMBER = '[0-9.edED]+'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_LBRACE = '{'
t_RBRACE = '}'
t_SEMI = ';'
t_ignore = ' \t'
t_PULS = r"\+"
t_MINUS = r"\-"
t_KAKE = r"\*"
t_WARU = r"\/"
t_EQUAL = r"\="


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def main():
    ase = open( sys.argv[1].split(".")[0]+".prs", "a" )
    ase.truncate(0)
    f = open(sys.argv[1], 'r')
    data = f.read()
    f.close()

    count = 1
    count2 = 0
    retcount = 0

    lexer.input(data)

    while True:
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
                    ase.write("\nmov "+arg+", "+tok.value)
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