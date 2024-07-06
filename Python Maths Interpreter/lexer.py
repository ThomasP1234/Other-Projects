from tokens import Token, TokenType
from string import ascii_letters

WHITESPACE = " \n\t"
DIGITS = "0123456789"
LETTERS = ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
KEYWORDS = [
    "VAR"
]

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.currentCharacter = next(self.text)
        except StopIteration:
            self.currentCharacter = None

    def generateTokens(self):
        while self.currentCharacter != None:
            if self.currentCharacter in WHITESPACE:
                self.advance()
            elif self.currentCharacter == "." or self.currentCharacter in DIGITS:
                yield self.generateNumber()
            elif self.currentCharacter in LETTERS:
                yield self.generateIdentifier()
            elif self.currentCharacter == "+":
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.currentCharacter == "-":
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.currentCharacter == "*":
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.currentCharacter == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.currentCharacter == "(":
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.currentCharacter == ")":
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.currentCharacter == "^":
                self.advance()
                yield Token(TokenType.POWER)
            elif self.currentCharacter == "!":
                self.advance()
                yield Token(TokenType.FACTORIAL)
            elif self.currentCharacter == "=":
                self.advance()
                yield Token(TokenType.EQUALS)
            else:
                raise Exception(f"Illegal Character '{self.currentCharacter}'")

    def generateNumber(self):
        decimalPointCount = 0 if self.currentCharacter != "." else 1
        numberStr = self.currentCharacter
        self.advance()

        while self.currentCharacter != None and (self.currentCharacter == '.' or self.currentCharacter in DIGITS):
            if self.currentCharacter == ".":
                decimalPointCount += 1
                if decimalPointCount > 1:
                    break

            numberStr += self.currentCharacter
            self.advance()

        if numberStr.startswith("."):
            numberStr = "0" + numberStr
        
        if numberStr.endswith("."):
            numberStr += "0"

        return Token(TokenType.NUMBER, float(numberStr))

    def generateIdentifier(self):
        identifierStr = self.currentCharacter
        self.advance()

        while self.currentCharacter != None and (self.currentCharacter in LETTERS_DIGITS + '_'):
            identifierStr += self.currentCharacter
            self.advance()

        if identifierStr in KEYWORDS:
            return Token(TokenType.KEYWORD, identifierStr)
        return Token(TokenType.IDENTIFIER, identifierStr)