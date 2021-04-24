from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *


# class ASTGeneration(CSELVisitor):
#     def visitProgram(self, ctx: CSELParser.ProgramContext):
#         return Program([VarDecl(Id(ctx.ID().getText()), [], NoneType(), None)])

# # bai 1 ast
# class ASTGeneration(CSELVisitor):

#     # program: vardecls EOF;
#     def visitProgram(self,ctx:CSELParser.ProgramContext):
#         return self.visit(ctx.vardecls()) +1 

#     # vardecls: vardecl vardecltail;
#     def visitVardecls(self,ctx:CSELParser.VardeclsContext):
#         return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

#     # vardecltail: vardecl vardecltail | ;
#     def visitVardecltail(self,ctx:CSELParser.VardecltailContext): 
#         if (ctx.getChildCount() == 2):
#             return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
#         return 0

    
#     # vardecl: mptype ids ';' ;    
#     def visitVardecl(self,ctx:CSELParser.VardeclContext): 
#         return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1

#     # mptype: INTTYPE | FLOATTYPE;    
#     def visitMptype(self,ctx:CSELParser.MptypeContext):
#         return 1

#     # ids: ID ',' ids | ID; 
#     def visitIds(self,ctx:CSELParser.IdsContext):
#         if (ctx.getChildCount() == 3):  
#             return 2 + self.visit(ctx.ids())
#         return 1
# # INTTYPE: 'int';

# # FLOATTYPE: 'float';

# # ID: [a-z]+ ;


# class ASTGeneration(CSELVisitor):
#     # program: vardecls EOF;
#     def visitProgram(self,ctx:CSELParser.ProgramContext):
#         return self.visit(ctx.vardecls()) +1
    
#     # vardecls: vardecl vardecltail;
#     def visitVardecls(self,ctx:CSELParser.VardeclsContext):
#         return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) + 2

#     # vardecltail: vardecl vardecltail | ;
#     def visitVardecltail(self,ctx:CSELParser.VardecltailContext): 
#         if (ctx.getChildCount() == 2):
#             return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())+2
#         return 1

#     # vardecl: mptype ids ';' ;
#     def visitVardecl(self,ctx:CSELParser.VardeclContext): 
#         return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 2


#     # mptype: INTTYPE | FLOATTYPE;
#     def visitMptype(self,ctx:CSELParser.MptypeContext):
#         return 0

#     # ids: ID ',' ids | ID;
#     def visitIds(self,ctx:CSELParser.IdsContext):
#         if (ctx.getChildCount() == 3 ):
#             return self.visit(ctx.ids()) + 1
#         return 0

#bai 3
class ASTGeneration(CSELVisitor):

    def visitProgram(self,ctx:CSELParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self,ctx:CSELParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:CSELParser.VardecltailContext): 
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
         
    def visitVardecl(self,ctx:CSELParser.VardeclContext): 
        typ = self.visit(ctx.mptype()) # tra ve inttype
        idslist = self.visit(ctx.ids()) # tra ve [Id(x), Id(y)
        #ket qua mong muong  [VarDecl(Id(x),IntType())]
        # cau distributetion dist(x,n)
    
        return [VarDecl(id,typ) for id in idslist]
        
        #hoac for id in idslist: resuild += [VarDecl(id,typ)]

    def visitMptype(self,ctx:CSELParser.MptypeContext):
        if ctx.INTTYPE() : 
            return IntType()
        else:
            return FloatType()

    def visitIds(self,ctx:CSELParser.IdsContext):
        if ctx.getChildCount()==3 :
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        else:
            return [Id(ctx.ID().getText())]

#bai4
# class ASTGeneration(CSELVisitor):
#     def visitProgram(self,ctx:CSELParser.ProgramContext):
#         return Program(self.visit(ctx.exp()))

#     def visitExp(self,ctx:CSELParser.ExpContext):
#         if (ctx.getChildCount() == 3):
#             return Binary(ctx.ASSIGN().getText() , self.visit(ctx.term()), self.visit(ctx.exp()))
#         return self.visit(ctx.term())

#     def visitTerm(self,ctx:CSELParser.TermContext):
#         if (ctx.getChildCount() == 3):
#             return Binary(ctx.COMPARE().getText() , self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
#         return self.visit(ctx.factor(0))

#     def visitFactor(self,ctx:CSELParser.FactorContext): 
#         if (ctx.getChildCount() == 3):
#             return Binary(ctx.ANDOR().getText() , self.visit(ctx.factor()), self.visit(ctx.operand()))
#         return self.visit(ctx.operand())

#     def visitOperand(self,ctx:CSELParser.OperandContext):
#         if (ctx.ID()):
#             return Id(ctx.ID().getText())
#         elif (ctx.INTLIT()):
#            return IntLiteral(int(ctx.INTLIT().getText()))
#         elif (ctx.BOOLIT()):
#             return BooleanLiteral(ctx.BOOLIT().getText())
#         else:
#            return self.visit(ctx.exp())

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;



