import numpy as np
import matplotlib.pyplot as p

import pandas as pd
from math import pi


def part2_1():
    data = np.genfromtxt('https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/1/6/1880-2017.csv', delimiter=',', dtype=None, names=True, skip_header=4) #skip_header=4 because first 4 lines from top are useless
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('Part 2-1: NOAA Land Ocean Temperature Anomalies')
    ax.set_xlabel('Year')
    ax.set_ylabel('Degrees F +/- From Average')
    ax.bar(data['Year'], data['Value'], color='r')
    p.show()
    

#Part 2-1
part2_1()