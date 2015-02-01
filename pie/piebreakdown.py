#!/usr/bin/python

from pylab import *
import csv

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

fracs = []
labels = []
colours = []
explode = []
stitle = "Pie Chart Title"

#read in from a file
datafile = open('piedata.csv', "rb")
reader = csv.reader(datafile)

for row in reader:
  fracs.append(row[0])
  labels.append(row[1])
  colours.append(row[2])
  explode.append(float(row[3]))
  
datafile.close()

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90, colors=colours)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title(stitle, bbox={'facecolor':'0.8', 'pad':5})

show()
