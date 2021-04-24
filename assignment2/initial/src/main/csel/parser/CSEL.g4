grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}
// bai 1 ast
// program: vardecls EOF;

// vardecls: vardecl vardecltail;

// vardecltail: vardecl vardecltail | ;

// vardecl: mptype ids ';' ;

// mptype: INTTYPE | FLOATTYPE;

// ids: ID ',' ids | ID; 

// INTTYPE: 'int';

// FLOATTYPE: 'float';

// ID: [a-z]+ ;

//bai 2 ast
// program: vardecls EOF;

// vardecls: vardecl vardecltail;

// vardecltail: vardecl vardecltail | ;

// vardecl: mptype ids ';' ;

// mptype: INTTYPE | FLOATTYPE;

// ids: ID ',' ids | ID; 

// INTTYPE: 'int';

// FLOATTYPE: 'float';

// ID: [a-z]+ ;

//bai 3 ast

program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail | ;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID; 

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

//bai 4

// program: exp EOF;

// exp: term ASSIGN exp | term;

// term: factor COMPARE factor | factor;

// factor: factor ANDOR operand | operand; 

// operand: ID | INTLIT | BOOLIT | '(' exp ')';

// INTLIT: [0-9]+ ;

// BOOLIT: 'True' | 'False' ;

// ANDOR: 'and' | 'or' ;

// ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

// COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

// ID: [a-z]+ ;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;