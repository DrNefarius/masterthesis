from evolution.geno import Geno


class Operator(object):
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity
        self.func = self.setFunction(arity)
        self.phenofunction = None

    def setFunction(self, arity):
        if arity == 1:
            return self.unary
        elif arity == 2:
            return self.binary
        else:
            raise ValueError(
                "Stelligkeitswert für Operatorfunktion nicht unterstützt (ist höher als 2 oder niedriger als 1)")

    def setPhenoFunc(self, function):
        self.phenofunction = function

    def unary(self, first):
        root = Geno(self.name)
        left = Geno(first) if isinstance(first, str) else first
        root.set_left(left)
        left.set_parent(root)
        return root

    def binary(self, first, second):
        root = Geno(self.name)
        left = Geno(first) if isinstance(first, str) else first
        right = Geno(second) if isinstance(second, str) else second
        root.set_left(left)
        root.set_right(right)
        left.set_parent(root)
        right.set_parent(root)
        return root
