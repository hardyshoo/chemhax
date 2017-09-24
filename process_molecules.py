import numpy as np

functionalGroups = ('ane', 'ene', 'yne', 'halo', 'ol', 'hydroxy', 'amine', 'amino','ether', 'alkoxy', 'al', 'one','oic acid', 'oate', 'amide')


def load_molecules(data_dir):
    with open(data_dir) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    content_s = [x.partition(',') for x in content]
    names = [x[0].strip() for x in content_s]
    formulae = [x[2].strip() for x in content_s]
    return names, formulae

def convert(name):
    name = name.lower()
    func_bools = np.zeros(len(functionalGroups))
    for i in range(len(functionalGroups)):
        if(functionalGroups[i] in name):
            func_bools[i] = 1
    return func_bools

def obtain_func_groups(names):
    return [convert(x) for x in names]

def codify(formula):
    '''Turns a molecular formula into an array containg the number of atoms of each element in the formula
    dict = {}
    start = 0
    mid = 0
    isdigit = 0
    for i in range(len(formula)):
        if (formula[i].isdigit()):
            if (isdigit == 0):
                isdigit = 1
                mid = i
        elif (isdigit == 1):
            isdigit = 0
            dict.update({formula[start:mid]:formula[mid:i]})
            start = i
        elif (i == len(formula) - 1):
            dict.update({formula[start:mid]:formula[mid:]})
    print(dict)
    '''
    return 1

def encode_formulae(formulae):
    return [codify(x) for x in formulae]
    
def main(fname):
    names, formulae = load_molecules(fname)
    funcs = obtain_func_groups(names)
    composit = encode_formulae(formulae)
    print('DONE!!!')
    #print(funcs)
    #print(formulae)

if __name__ == '__main__':
    main("Molecules.csv")
