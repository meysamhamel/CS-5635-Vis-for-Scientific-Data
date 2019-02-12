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

def plot_line_graph( ):
    diagram.plot(new)
    diagram.xlabel('Number')
    diagram.ylabel('Uniformly distributed random numbers')
    diagram.show()
    print(new)


plot_line_graph()


# End of Q3

