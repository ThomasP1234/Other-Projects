from nodes import *
from math import pi, e

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.constants()
        # self.parent = None

    def constants(self):
        self.set("null", NumberNode(0))
        self.set("pi", pi)
        self.set("e", e)
        self.set("phi", (1+(5)**0.5)/2)

    def get(self, name):
        value = self.symbols.get(name, None)
        # if value == None and self.parent:
        #     return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]