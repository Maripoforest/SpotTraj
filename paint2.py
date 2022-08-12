import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np 
from pylab import *

xcen = 0.9658
ycen = 0.7558
colors = ['orange', 'blue', 'purple', 'pink', 'green', 'brown']
# filename = ['ori/ori1.csv', 'ori/ori2.csv', 'ori/ori3.csv']
filename = ['data/xinyu_ori0.csv', 'data/xinyu_ori1.csv', 'data/xinyu_step.csv', 'data/xinyu_gaze.csv', 'data/xinyu_tilt.csv']
# filename = ['data/rongyu_ori0.csv', 'data/rongyu_ori1.csv', 'data/rongyu_step.csv', 'data/rongyu_gaze.csv']
x = []
y = []
for i in range(len(filename)):
    x.append([])
    y.append([])
d = []
for i in range(len(filename)):
    file = open(filename[i])
    csvreader = csv.reader(file)
    distance = 100
    header = []
    header = next(csvreader)
    for row in csvreader:
        xa = float(row[1]) - xcen
        ya = float(row[2]) - ycen
        x[i].append(xa)
        y[i].append(ya)
        d_temp = np.sqrt(xa*xa + ya*ya)
        if d_temp < distance:
            distance = d_temp
    d.append(distance)
print(len(d))
figure(dpi = 150)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
scatter(0,0, color = 'red', linewidth=2.5, linestyle='--')
cir = []
for i in range(len(d)):
    cir.append(Circle(xy = (0.0, 0.0), radius = d[i], alpha = 0.4 * float(1.1 - d[i]/max(d)), color = 'red'))
    ax.add_patch(cir[i])
    plot(y[i], x[i], color = colors[i], label = filename[i])
legend()
show()