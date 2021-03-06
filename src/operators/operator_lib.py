from operators.operator import Operator
from src.evolution.phenotype import Phenotype
from src import constants


class OperatorLib(object):
    """Defines all operators and saves them in a list for easy access."""

    def __init__(self):
        self.operators = []
        self.populate()

    def get_operators(self):
        return self.operators

    def populate(self):
        self.addSEQ()
        self.addPAR()
        self.addDOUB()
        self.addHALF()

        if constants.USE_CNN:
            self.addMAX_P()
            self.addDROP_DEC()
            self.addDROP_INC()
            self.addFILTER_DEC()
            self.addFILTER_INC()
            self.addKER_SIZE_DEC()
            self.addKER_SIZE_INC()
            self.addPOOL_SIZE_DEC()
            self.addPOOL_SIZE_INC()
        else:
            self.addSOFTMAX()
            self.addELU()
            self.addSOFTPLUS()
            self.addSOFTSIGN()
            self.addRELU()
            self.addTANH()
            self.addSIGMOID()
            self.addHSIGMOID()

    # Standard operators

    def addSEQ(self):
        operator = Operator('SEQ', 2)

        def func(node, index):
            next = Phenotype(index, node.neurons)
            next.add_input(node)
            next.copy_outputs(node)
            for n in node.outputs:
                n.inputs.remove(node)
            node.outputs = []
            node.add_output(next)
            return node, next  # return LEFT, RIGHT

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addPAR(self):
        operator = Operator('PAR', 2)

        def func(node, index):
            next = Phenotype(index, node.neurons)
            next.copy_inputs(node)
            next.copy_outputs(node)
            return node, next  # return LEFT, RIGHT

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addDOUB(self):
        operator = Operator('DOUB', 1)

        def func(node):
            node.multiply_neuron_count(2)
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addHALF(self):
        operator = Operator('HALF', 1)

        def func(node):
            node.divide_neuron_count(2)
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    # Convolutional operators

    def addMAX_P(self):
        operator = Operator('MAX_P', 1)

        def func(node):
            node.maxPooling = True
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addDROP_DEC(self):
        operator = Operator('DROP_DEC', 1)

        def func(node):
            if node.dropout > 0.1:  # make sure that it never reaches 0%
                node.dropout -= 0.1
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addDROP_INC(self):
        operator = Operator('DROP_INC', 1)

        def func(node):
            if node.dropout < 0.9:  # make sure that it never reaches 100%
                node.dropout += 0.1
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addFILTER_INC(self):
        operator = Operator('FILTER_INC', 1)

        def func(node):
            node.filter_count *= 2
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addFILTER_DEC(self):
        operator = Operator('FILTER_DEC', 1)

        def func(node):
            if node.filter_count > constants.FILTER_COUNT_MIN:  # make sure that it stays at least FILTER_COUNT_MIN
                node.filter_count = int(node.filter_count / 2)
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addKER_SIZE_INC(self):
        operator = Operator('KER_SIZE_INC', 1)

        def func(node):
            if node.kernel_size < constants.IMG_DIMENSION:
                node.kernel_size += 2  # make sure kernel always stays uneven (e.g. 3, 5, 7 etc.) for convolution to work
                if node.kernel_size > constants.IMG_DIMENSION:  # addition could lead to out of bounds
                    node.kernel_size -= 2
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addKER_SIZE_DEC(self):
        operator = Operator('KER_SIZE_DEC', 1)

        def func(node):
            if node.kernel_size > constants.KERNEL_SIZE_MIN:  # make sure kernel stays at least KERNEL_SIZE_MIN
                node.kernel_size -= 2  # make sure it always stays uneven (e.g. 3, 5, 7 etc.) for convolution to work
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addPOOL_SIZE_INC(self):
        operator = Operator('POOL_SIZE_INC', 1)

        def func(node):
            if node.pool_size < constants.IMG_DIMENSION:  # prevent out of bounds
                node.pool_size += 1
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addPOOL_SIZE_DEC(self):
        operator = Operator('POOL_SIZE_DEC', 1)

        def func(node):
            if node.pool_size > constants.POOL_SIZE_MIN:  # make sure it always stays at least POOL_SIZE_MIN
                node.pool_size -= 1
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    # activation function operators

    def addSOFTMAX(self):
        operator = Operator('SOFTMAX', 1)

        def func(node):
            node.set_activation('softmax')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addELU(self):
        operator = Operator('ELU', 1)

        def func(node):
            node.set_activation('elu')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addSOFTPLUS(self):
        operator = Operator('SOFTPLUS', 1)

        def func(node):
            node.set_activation('softplus')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addSOFTSIGN(self):
        operator = Operator('SOFTSIGN', 1)

        def func(node):
            node.set_activation('softsign')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addRELU(self):
        operator = Operator('RELU', 1)

        def func(node):
            node.set_activation('relu')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addTANH(self):
        operator = Operator('TANH', 1)

        def func(node):
            node.set_activation('tanh')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addSIGMOID(self):
        operator = Operator('SIGMOID', 1)

        def func(node):
            node.set_activation('sigmoid')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    def addHSIGMOID(self):
        operator = Operator('HSIGMOID', 1)

        def func(node):
            node.set_activation('hard_sigmoid')
            return node

        operator.set_pheno_func(func)
        self.operators.append(operator)

    # generic getter
    def getOperator(self, name):
        for n in self.operators:
            if n.name == name:
                return n
