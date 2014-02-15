# access the bump sensor
spinn.make_bump(net, 'bumpsensor')
# create a group of 100 neurons to represent the
#  bump sensor data as a 2-dimensional value
net.make('bump', neurons=100, dimensions=2)
# define the transformation matrix and connect the neurons
row1 = [cos(i*2*pi/6) for i in range(6)]
row2 = [sin(i*2*pi/6) for i in range(6)]
net.connect('bumpsensor', 'bump', transform=[row1, row2])

# create the combined neural population
net.make('state', neurons=1000, dimensions=6)
# connect individual sensors into combined state
#  with appropriate transformations
net.connect('bump', 'state', 
            transform=[[1,0,0,0,0,0],[0,1,0,0,0,0]])
net.connect('vision', 'state', 
            transform=[[0,0,1,0,0,0],[0,0,0,1,0,0]])
net.connect('move', 'state', 
            transform=[[0,0,0,0,1,0],[0,0,0,0,0,1]])

            