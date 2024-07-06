from math import factorial
from nodes import *
from value import *

class Interpreter:
    def __init__(self, symbolTable):
        self.symbolTable = symbolTable
        self.solveMode = [False,"None"]

    def visit(self, node):
        methodName = f"visit{type(node).__name__}"
        method = getattr(self, methodName)
        return method(node)

    def visitNumberNode(self, node):
        return Number(node.value)

    def visitAccessNode(self, node):
        if self.solveMode[0] == True and self.symbolTable.in_(node.name) != 2:
            if self.solveMode[1] != "None" and self.solveMode[1] != node.name:
                raise Exception(f"Can only solve for 1 unknown")
            if value:=self.symbolTable.get(self.solveMode[1]):
                return value
            self.solveMode[1] = node.name
            self.symbolTable.set(node.name, Number(1))
            return self.symbolTable.get(node.name)
        else:
            if value:=self.symbolTable.get(node.name):
                return value
            if self.solveMode[0] == False:
                raise Exception(f"{node.name} is not defined")

    def visitAssignNode(self, node):
        self.symbolTable.set(node.name, value:=self.visit(node.value))
        return Number(value)

    def visitSolveNode(self, node):
        self.solveMode[0] = True
        i = 0
        h=10**-10
        while i<10:
            lhs = self.visit(node.node1).value
            rhs = self.visit(node.node2).value
            fx = lhs-rhs
            x = self.symbolTable.get(self.solveMode[1])
            self.symbolTable.set(self.solveMode[1], Number(x.value+h))
            lhs2 = self.visit(node.node1).value
            rhs2 = self.visit(node.node2).value
            fxh=lhs2-rhs2
            
            try:
                x_new = x.value - ( fx ) / ( ( (fxh) - (fx) ) / (h) )
            except ZeroDivisionError:
                raise Exception("Cannot compute a solution - does one exist?")

            x = Number(x_new)
            self.symbolTable.set(self.solveMode[1], x)
            i+=1
        x = Number(round(100000*x.value)/100000)
        self.symbolTable.set(self.solveMode[1], x)
        lhs = self.visit(node.node1).value
        rhs = self.visit(node.node2).value
        if round(100*(lhs-rhs))/100!=0:
            raise Exception("No real solutions have been found")
        return x
    
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
            number = self.visit(node.node1).value
            if int(number) != number:
                raise TypeError
            number = int(number)
            if number < 0:
                raise ValueError
            return Number(factorial(number))
        except TypeError or ValueError:
            raise Exception("Factorial only accepts positive integer values")

    def visitPlusNode(self, node):
        return self.visit(node.node)

    def visitMinusNode(self, node):
        return Number(self.visit(node.node).value*-1)