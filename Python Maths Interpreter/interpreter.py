from math import factorial
from nodes import *
from value import *

class Interpreter:
    def __init__(self, symbolTable):
        self.symbolTable = symbolTable

    def visit(self, node):
        methodName = f"visit{type(node).__name__}"
        method = getattr(self, methodName)
        return method(node)

    def visitNumberNode(self, node):
        return Number(node.value)

    def visitAccessNode(self, node):
        if value:=self.symbolTable.get(node.name):
            return value
        raise Exception(f"{node.name} is not defined")

    def visitAssignNode(self, node):
        self.symbolTable.set(node.name, value:=self.visit(node.value))
        return Number(value)

    def visitAddNode(self, node):
        return Number(self.visit(node.node1).value + self.visit(node.node2).value)

    def visitSubtractNode(self, node):
        return Number(self.visit(node.node1).value - self.visit(node.node2).value)

    def visitMultiplyNode(self, node):
        return Number(self.visit(node.node1).value * self.visit(node.node2).value)

    def visitDivideNode(self, node):
        try:
            return Number(self.visit(node.node1).value / self.visit(node.node2).value)
        except ZeroDivisionError:
            raise Exception("Division by zero is not allowed")

    def visitPowerNode(self, node):
        return Number(self.visit(node.node1).value ** self.visit(node.node2).value)

    def visitFactorialNode(self, node):
        try:
            return Number(factorial(self.visit(node.node1).value))
        except TypeError or ValueError:
            raise Exception("Factorial only accepts positive integer values")

    def visitPlusNode(self, node):
        return self.visit(node.node)

    def visitMinusNode(self, node):
        return Number(self.visit(node.node).value*-1)