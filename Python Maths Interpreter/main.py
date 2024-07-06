from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
from symbol_table import SymbolTable

symbolTable = SymbolTable()

while True:
    try:
        text = input(":")
        lexer = Lexer(text)
        tokens = lexer.generateTokens()
        parser = Parser(tokens)
        tree = parser.parse()
        # print(tree)
        if not tree: continue
        interpreter = Interpreter(symbolTable)
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)