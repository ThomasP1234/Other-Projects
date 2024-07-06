from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raiseError(self):
        raise Exception("Invalid Syntax")

    def advance(self):
        try:
            self.currentToken = next(self.tokens)
        except StopIteration:
            self.currentToken = None

    def parse(self):
        if self.currentToken == None:
            return None

        result = self.expr()

        if self.currentToken != None:
            self.raiseError()

        return result

    def expr(self):
        if self.currentToken.type == TokenType.KEYWORD and self.currentToken.value == "VAR":
            self.advance()
            if self.currentToken.type != TokenType.IDENTIFIER:
                self.raiseError()
            identifier = self.currentToken.value
            self.advance()
            if self.currentToken.type != TokenType.EQUALS:
                self.raiseError()
            self.advance()
            result = AssignNode(identifier, self.expr())
            return result

        if self.currentToken.type == TokenType.KEYWORD and self.currentToken.value == "SOLVE":
            self.advance()
            lhs = self.expr()
            if self.currentToken.type != TokenType.EQUALS:
                self.raiseError()
            self.advance()
            result = SolveNode(lhs, self.expr())
            return result
        
        if self.currentToken.type == TokenType.KEYWORD and self.currentToken.value == "HELP":
            self.advance()
            if self.currentToken.type != TokenType.KEYWORD:
                self.raiseError()
            result = HelpNode(self.currentToken.value)
            self.advance()
            return result

        result = self.term()

        while self.currentToken != None and self.currentToken.type in (TokenType.PLUS,TokenType.MINUS):
            if self.currentToken.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.currentToken.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.currentToken != None and self.currentToken.type in (TokenType.MULTIPLY,TokenType.DIVIDE):
            if self.currentToken.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.currentToken.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.currentToken

        if token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        return self.power()
    
    def power(self):
        result = self.atom()

        if self.currentToken != None and self.currentToken.type == TokenType.POWER:
            self.advance()
            return PowerNode(result, self.factor())

        elif self.currentToken != None and self.currentToken.type == TokenType.FACTORIAL:
            self.advance()
            return FactorialNode(result)

        return result

    def atom(self):
        token = self.currentToken

        if token.type == TokenType.NUMBER:
            self.advance()
            if self.currentToken!= None and self.currentToken.type in (TokenType.LPAREN, TokenType.IDENTIFIER):
                variable = self.power()
                # if self.currentToken != None and self.currentToken.type == TokenType.LPAREN:
                #     return MultiplyNode(NumberNode(token.value), self.factor())
                # if self.currentToken != None and self.currentToken.type == TokenType.IDENTIFIER:
                #     self.advance()
                #     if self.currentToken != None and self.currentToken.type == TokenType.LPAREN:
                #         return MultiplyNode(MultiplyNode(NumberNode(token.value), variable), self.factor())
                return MultiplyNode(NumberNode(token.value), variable)
            return NumberNode(token.value)

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            if self.currentToken != None and self.currentToken.type == TokenType.LPAREN:
                return MultiplyNode(AccessNode(token.value), self.factor())
            return AccessNode(token.value)

        elif token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.currentToken.type != TokenType.RPAREN:
                self.raiseError()

            self.advance()
            if self.currentToken != None and self.currentToken.type == TokenType.LPAREN:
                result = MultiplyNode(result, self.expr())

            return result

        self.raiseError()