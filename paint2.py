import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np 
from pylab import *

xcen = 0.9658
ycen = 0.7558
time = []
x = [[],[],[]]
y = [[],[],[]]
d = []
colors = ['orange', 'blue', 'purple', 'pink']
filename = ['ori/ori1.csv', 'ori/ori2.csv', 'ori/ori3.csv']
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
print(d)
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
for i in range(len(x)):
    cir.append(Circle(xy = (0.0, 0.0), radius = d[i], alpha = 0.3 * float(d[i]/max(d)), color = colors[i]))
    ax.add_patch(cir[i])
    plot(y[i], x[i], color = colors[i], label = 'ori'+str(i))
legend()
show()