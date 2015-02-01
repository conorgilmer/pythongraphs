import pylab, csv

def drawGraph(xData,yData) :
	pylab.figure(1)
	pylab.plot(xData,yData)
	pylab.show()

pylab.title('blab blah', fontsize =25)
pylab.xlabel('X numbers')
pylab.ylabel('Y Numbers')




xstuff =[]
ystuff =[]

dataFile = open('linedata.csv', "rb")
reader = csv.reader(dataFile)

rownum = 0
for row in reader:
  xstuff.append(row[0])
  ystuff.append(row[1])

dataFile.close()

print "xstuff" 
print xstuff
print "ystuff"
print ystuff

drawGraph(xstuff, ystuff)
