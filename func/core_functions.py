from math import sqrt
from random import choice


def mean(a):
    # a - the transferable sample
    return sum(a) / len(a)


def dispersion(a):
    dispersion_output = 0
    b = mean(a)
    for i in a:
        dispersion_output += (i - b) ** 2

    return dispersion_output / (len(a) - 1)


def standard_deviation(a):
    # a - dispersion
    return sqrt(a)


def z_evaluation(x, m, q):
    # x - the  figure you want to examine
    # m - the mean
    # q - the standard deviation
    return (x - m) / q


def simple_random_sample(a, r):
    # a - the general population
    # r - number of items in the sample
    return_list = []
    for i in range(r):
        to_sample = choice(a)
        a.remove(to_sample)
        return_list.append(to_sample)
    return return_list

