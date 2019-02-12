
#part1_3
import numpy as np
import matplotlib.pyplot as diagram 
from numpy.random import *
import matplotlib.mlab as mlab
from tempfile import TemporaryFile
#Create 100 random number uniformaly dis 
# Return them in binary file.

def create_unif():
    array = np.random.uniform(0, 100, 100) # Generate the random numbers
    outfile = TemporaryFile()
    # Save the binary file
    np.save(outfile, array) 
    outfile.seek(0)
    return outfile


new = np.load(create_unif())

def plot_histogram_2():
    fig = diagram.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(new, bins=7)
    ax.set_title('Histogram')
    ax.set_xlabel('X')
    ax.set_ylabel('frequancy')
    fig.show()


plot_histogram_2()

