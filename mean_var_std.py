import numpy as np


def calculate(input_list):
    if len(input_list) < 9:
        raise ValueError('List must contain nine numbers.')

    a = np.array(input_list).reshape((3, 3))
    numpy_functions = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    calculations = {'mean': [], 'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}

    for func, key in zip(numpy_functions, calculations):
        calculations[key].append(list(func(a, axis=0)))
        calculations[key].append(list(func(a, axis=1)))
        calculations[key].append(func(a, axis=None))

    return calculations
