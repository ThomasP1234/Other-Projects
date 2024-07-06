from nodes import *
from math import pi, e

class ConstantTable:
    def __init__(self):
        self.symbols = {}
        self.set("pi", NumberNode(pi))
        self.set("e", NumberNode(e))
        self.set("phi", NumberNode((1+(5)**0.5)/2))
        
    def get(self, name):
        value = self.symbols.get(name, None)
        return value
    
    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]

    def in_(self, name):
        if name in self.symbols:
            return True
        return False

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = ConstantTable()

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]

    def in_(self, name):
        if name in self.symbols:
            return 1
        if self.parent.in_(name):
            return 2
        return 0