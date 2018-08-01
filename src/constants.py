DEBUG = False
USE_CNN = False

DATASET = 'MNIST'  # DATASET can be either 'MNIST' or 'CIFAR10'

TRAIN_SIZE = 5000  # fallback parameter if no valid DATASET is declared
IMG_DIMENSION = 28  # fallback parameter if no valid DATASET is declared

FILTER_COUNT = 32
DROPOUT = 0.5
KERNEL_SIZE = 3
POOL_SIZE = 2

if DATASET == 'MNIST':
    TRAIN_SIZE = 6000  # 60000 standard
    IMG_DIMENSION = 28
elif DATASET == 'CIFAR10':
    TRAIN_SIZE = 50000  # 50000 standard
    IMG_DIMENSION = 32

if USE_CNN:
    INPUT_DIMENSION = [IMG_DIMENSION, 1]
else:
    INPUT_DIMENSION = IMG_DIMENSION * IMG_DIMENSION
OUTPUT_DIMENSION = 10
BATCH_SIZE = 128

POPS = 15  # Number of Populations
NGEN = 1  # Number of Generations
MUTPB = 0.1  # Probability of Mutation
CXPB = 0.5  # Probability of Crossover
BLOAT_LIMIT = 17

NEURONS = 100
ACTIVATION_FUNCTION = 'relu'  # standard activation function
MIN_NEURONS = NEURONS
MAX_NEURONS = 10000

# Keras stuff
K_ACTIVATION_FUNCTION_OUTPUT_LAYER = 'softmax'
K_OPTIMIZER = 'adam'
K_LOSS = 'categorical_crossentropy'
K_EPOCHS = 25
K_CLASS_COUNT = OUTPUT_DIMENSION
K_VERBOSE = 0  # 0 = silent || 1 = progress bar || 2 = show epoch

BASE_LINK = "C:\\Users\\Tobias\\PycharmProjects\\master\\src"
GENOTYPE_PATH = BASE_LINK + '\\output\\Genotype.txt'
PHENOTYPE_PATH = BASE_LINK + '\\output\\Phenotype.txt'
GENGRAPH_PATH = BASE_LINK + '\\output\\gen.png'
KERASGRAPH_PATH = BASE_LINK + '\\output\\keras.png'
