# python -m unittest interpreter_test

import unittest
from math import factorial
from nodes import *
from interpreter import Interpreter
from value import *
from symbol_table import SymbolTable
import random

class TestInterpreter(unittest.TestCase):
    symbolTable = SymbolTable()

    def testNumbers(self):
        value = Interpreter(self.symbolTable).visit(NumberNode(10.0))
        self.assertEqual(value, Number(10.0))

    def testIndividualOperations(self):
        value = Interpreter(self.symbolTable).visit(AddNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(num2:=random.uniform(1,100))))
        self.assertEqual(value, Number(num1+num2))

        value = Interpreter(self.symbolTable).visit(SubtractNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(num2:=random.uniform(1,100))))
        self.assertEqual(value, Number(num1-num2))

        value = Interpreter(self.symbolTable).visit(MultiplyNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(num2:=random.uniform(1,100))))
        self.assertEqual(value, Number(num1*num2))

        value = Interpreter(self.symbolTable).visit(DivideNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(num2:=random.uniform(1,100))))
        self.assertEqual(value, Number(num1/num2))

        with self.assertRaises(Exception):
            value = Interpreter(self.symbolTable).visit(DivideNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(0.0)))

        value = Interpreter(self.symbolTable).visit(PowerNode(NumberNode(num1:=random.uniform(1,100)), NumberNode(num2:=random.uniform(1,100))))
        self.assertEqual(value, Number(num1**num2))

        value = Interpreter(self.symbolTable).visit(FactorialNode(NumberNode(num1:=random.randint(1,10))))
        self.assertEqual(value, Number(float(factorial(num1))))

        with self.assertRaises(Exception):
            value = Interpreter(self.symbolTable).visit(FactorialNode(NumberNode(num1:=random.uniform(-10,10))))

    def testVariables(self):
        self.symbolTable.set("x", Number(1.0))
        value = Interpreter(self.symbolTable).visit(AssignNode("x", AddNode(AccessNode("x"), NumberNode(1.0))))
        self.assertEqual(value, Number(2.0))

    def testFullExpression(self):
        tree = AddNode(
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
                    NumberNode(10.0)))

        result = Interpreter(self.symbolTable).visit(tree)
        self.assertEqual(result.value, 3628890.0)