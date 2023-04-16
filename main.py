import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 12]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'blue', 'orange' ]
explodelist = [0.0, 0.0, 0.0, 0.1]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 45)
plot.axis('equal')
plot.savefig('piechart.png')
