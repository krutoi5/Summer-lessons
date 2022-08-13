
def funct(func):

    def fst(*a, **b):
        print('старт')
        func(a, b)
        print('конец')
    return fst

@funct
def sey(a, b):
    print('hello word')
    print(a)
    print(b)

@funct
def seu(a, b):
    print(a)
    print(b) 

sey('esf', 'sef')
seu('wa', 'wad')