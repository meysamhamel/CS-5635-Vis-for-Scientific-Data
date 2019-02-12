#part1_2
import numpy as np
import matplotlib.pyplot as p
from numpy.random import *
import matplotlib.mlab as mlab
from tempfile import TemporaryFile
def create_rand_arr():
    array = []
    for x in range(10000):
        array.append(randint(10, 1000))
    return array


rand_arr = create_rand_arr()


def p_histogram():
    fig = p.figure()
    fig.patch.set_facecolor('red')
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(rand_arr, bins=20)
    ax.set_title('Q2: Histogram for (10, 1000)')
    ax.set_xlabel('X')
    ax.set_ylabel('FREQUENCY')
    #bins, patches = p.hist(x, color='green')
    fig.show()


p_histogram()
