import csv
import matplotlib.pyplot as plt
import numpy as np 
from pylab import *

xcen = 0.9658
ycen = 0.7558
colors = ['green', 'blue', 'orange', 'pink', 'red', 'brown']
filenames = []
filenames.append(['ori/ori1.csv', 'data/xinyu_ori0.csv', 'data/rongyu_ori0.csv'])
filenames.append(['ori/ori2.csv', 'data/xinyu_ori1.csv', 'data/rongyu_ori1.csv',])
filenames.append(['ori/gaze.csv', 'data/xinyu_gaze.csv', 'data/rongyu_gaze.csv'])
filenames.append(['ori/step.csv', 'data/xinyu_step.csv', 'data/rongyu_step.csv', ])
fnames = ['orientation1', 'orientation2', 'gaze', 'step']
x = []
y = []
names = []

for filename in filenames:
    for i in range(len(filename)):
        x.append([])
        y.append([])
        
w = list(range(len(filenames[0])))
j = 0
p = 0
for filename in filenames:
    d = []

    for i in range(len(filename)):
        file = open(filename[i])
        csvreader = csv.reader(file)
        distance = 100
        header = []
        header = next(csvreader)
        for row in csvreader:
            if (row[1] != '0.0'):
                xa = float(row[1]) - xcen
                ya = float(row[2]) - ycen
                d_temp = np.sqrt(xa*xa + ya*ya)
                if d_temp < distance:
                    distance = d_temp
            else:
                distance = 0
        d.append(distance)
    print(d)
    print(p)
    plt.bar(w, d, width = 0.1, label = fnames[p],  fc = colors[j])
    j += 1
    p += 1
    for i in range(len(w)):
        w[i] = w[i] + 0.1
plt.xlabel("participant A                     participant B                     participant C ")
plt.legend()
plt.show()