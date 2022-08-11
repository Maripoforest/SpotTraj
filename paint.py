import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np 
from pylab import *

xcen = 0.9658
ycen = 0.7558

file = open('ori1.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

time = []
x = []
y = []
distance = 100

for row in csvreader:
    time.append(row[0])
    xa = float(row[1]) - xcen
    ya = float(row[2]) - ycen
    x.append(xa)
    y.append(ya)
    d_temp = np.sqrt(xa*xa + ya*ya)
    if d_temp < distance:
        distance = d_temp

file = open('step.csv')
csvreader2 = csv.reader(file)
header2 = []
header2 = next(csvreader2)
distance2 = 100

x2 = []
y2 = []

for row2 in csvreader2:
    xa2 = float(row2[1]) - xcen
    ya2 = float(row2[2]) - ycen
    x2.append(xa2)
    y2.append(ya2)
    d_temp2 = np.sqrt(xa2*xa2 + ya2*ya2)
    if d_temp2 < distance2:
        distance2 = d_temp2

figure(dpi = 150)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
scatter(0,0, color = 'red', linewidth=2.5, linestyle='--')
cir1 = Circle(xy = (0.0, 0.0), radius = distance, alpha = 0.2, color = 'red')
cir2 = Circle(xy = (0.0, 0.0), radius = distance2, alpha = 0.4, color = 'red')
ax.add_patch(cir1)
ax.add_patch(cir2)
plot(y, x, color = 'blue')
plot(y2, x2, color = 'green')
show()