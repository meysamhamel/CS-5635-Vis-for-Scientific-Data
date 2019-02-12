#part1_1
import numpy as np
import matplotlib.pyplot as p
from numpy.random import *
import matplotlib.mlab as mlab
from tempfile import TemporaryFile


#make new arry with order
def new_array_in_sort():
    array = np.array(range(1, 101))
    return array


def show_p_graph():
    array = new_array_in_sort()
    p.boxplot(array)

    p.show()


show_p_graph()

