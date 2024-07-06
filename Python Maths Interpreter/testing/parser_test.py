# python -m unittest parser_test

import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *
import random

class TestParse(unittest.TestCase):

    def testEmpty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def testNumbers(self):
        tokens = [Token(TokenType.NUMBER, x:=float(random.randint(1, 100)))]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(x))

    def testIndividualOperations(self):
        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 10)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(10.0), NumberNode(10.0)))
        
        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 10)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(10.0), NumberNode(10.0)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 10)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(10.0), NumberNode(10.0)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 10)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(10.0), NumberNode(10.0)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.POWER),
            Token(TokenType.NUMBER, 10)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, PowerNode(NumberNode(10.0), NumberNode(10.0)))

        tokens = [
            Token(TokenType.NUMBER, 10),
            Token(TokenType.FACTORIAL)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, FactorialNode(NumberNode(10.0)))

    def testVariables(self):
        tokens = [
            Token(TokenType.KEYWORD, "VAR"),
            Token(TokenType.IDENTIFIER, "x"),
            Token(TokenType.EQUALS),
            Token(TokenType.IDENTIFIER, "x"),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 1)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AssignNode("x", AddNode(AccessNode("x"), NumberNode(1))))

    def testFullExpression(self):
        tokens = [
            # 10! + 10 * (10^2 - 10) / 10
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.FACTORIAL),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.MULTIPLY),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.POWER),
            Token(TokenType.NUMBER, 2.0),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.RPAREN),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 10.0)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            FactorialNode(
                NumberNode(10.0)),
            DivideNode(
                MultiplyNode(
                    NumberNode(10.0),
                    SubtractNode( 
                        PowerNode(
                            NumberNode(10.0),
                            NumberNode(2.0),
                        ),
                        NumberNode(10.0))), 
                NumberNode(10.0))
            ))
        
