import numpy as np
from scipy.integrate import dblquad
from matplotlib import pyplot as plt
import csv

# Start by getting some data plotted...
path = '~/Documents/AB_RANS_Data/SingleCar'

with open(path + '/Rear Plane.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
