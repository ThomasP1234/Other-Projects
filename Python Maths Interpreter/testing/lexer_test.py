# python -m unittest lexer_test

import unittest
from tokens import Token, TokenType
from lexer import Lexer
import random

class TestLexer(unittest.TestCase):
    def test_Empty(self):
        tokens = list(Lexer("").generateTokens())
        self.assertEqual(tokens, [])

    def test_WhitespaceSpace(self):
        tokens = list(Lexer(" "*random.randint(1,10)).generateTokens())
        self.assertEqual(tokens, [])

    def test_WhitespaceLine(self):
        tokens = list(Lexer("\n"*random.randint(1,10)).generateTokens())
        self.assertEqual(tokens, [])

    def test_WhitespaceTab(self):
        tokens = list(Lexer("\t"*random.randint(1,10)).generateTokens())
        self.assertEqual(tokens, [])

    def test_WhitespaceMix(self):
        tokens = list(Lexer(" "*random.randint(1,10)+"\n"*random.randint(1,10)+"\t"*random.randint(1,10)).generateTokens())
        self.assertEqual(tokens, [])

    def test_Numbers(self):
        numbers = [random.randint(1,100),random.uniform(1,100), "."+str(random.randint(1,100)), str(random.randint(1,100))+".", "."]
        tokens = list(Lexer(' '.join(str(number) for number in numbers)).generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, float(numbers[0])),
            Token(TokenType.NUMBER, numbers[1]),
            Token(TokenType.NUMBER, float(numbers[2])),
            Token(TokenType.NUMBER, float(numbers[3])),
            Token(TokenType.NUMBER, 0.0)
        ])

    def test_Operators(self):
        tokens = list(Lexer("+-*/^!").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
            Token(TokenType.POWER),
            Token(TokenType.FACTORIAL)
        ])

    def test_Parens(self):
        tokens = list(Lexer("()").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN)
        ])

    def test_Variables(self):
        tokens = list(Lexer("VAR SOLVE x y z").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.KEYWORD, "VAR"),
            Token(TokenType.KEYWORD, "SOLVE"),
            Token(TokenType.IDENTIFIER, "x"),
            Token(TokenType.IDENTIFIER, "y"),
            Token(TokenType.IDENTIFIER, "z")
        ])

    def test_All(self):
        tokens = list(Lexer("12x +\t\n(16 / 14 * 12) - 6^7!").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.IDENTIFIER, "x"),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 16),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.RPAREN),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 6),
            Token(TokenType.POWER),
            Token(TokenType.NUMBER, 7),
            Token(TokenType.FACTORIAL)
        ])