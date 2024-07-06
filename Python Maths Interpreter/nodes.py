from dataclasses import dataclass

@dataclass
class NumberNode:
    value:float

    def __repr__(self):
        return f"({self.value})"

@dataclass
class AccessNode:
    name: any

    def __repr__(self):
        return f"({self.value})"

@dataclass
class AssignNode:
    name: any
    value: any

    def __repr__(self):
        return f"({self.name}={self.value})"

@dataclass
class AddNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} + {self.node2})"

@dataclass
class SubtractNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} - {self.node2})"

@dataclass
class MultiplyNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} * {self.node2})"

@dataclass
class DivideNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} / {self.node2})"

@dataclass
class PowerNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} ^ {self.node2})"

@dataclass
class FactorialNode:
    node1: any

    def __repr__(self):
        return f"({self.node1}!)"

@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"