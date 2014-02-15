import sys
import pylab as m
sys.path.append('/opt/nengo/python')
import stats
import numpy as np

reader=stats.Reader('ResultTrain-')

import math
def filter(data, tau):
    decay = math.exp(-0.01/tau)
    data = np.array(data)
    for i in range(len(data)-1):
        data[i+1] = data[i+1]*(1-decay)+data[i]*decay
    return data    

    
print reader.time.shape
print reader.sensors.shape

plot = stats.plot.time.Time(reader.time-8, time_range=(0,7), border_left=1.2, height=5)

state=filter(reader.sensors[:,2:8], 0.2)

import syde556
a = syde556.Ensemble(neurons=1000, dimensions=6, seed=1)
d = a.compute_decoder(state.T, state.T)
A, xhat2 = a.simulate_spikes(state.T, d, tau=0.1)

plot.add('motor\ntraining\ndata', filter(reader.correct, 0.2), range=(-1.2, 1.2))
plot.add('sensor\nstate', filter(reader.sensors[:,2:8], 0.2), range=(-1.7, 1.7))
plot.add_spikes('neural\nactivity\n\n', A, sample=100, cluster=False, merge=20, contrast_scale=0.5)
plot.add('decoded\nneural\nactivity', filter(reader.drive, 0.01))

plot.save('sensorimotor.png', dpi=600)
plot.show()

"""
    
    
plots = 6

t = reader.time

m.figure(figsize=(10,8))

m.subplot(plots, 1, 1)
m.plot(t, filter(reader.sensors[:,:2], 0.01))
m.ylabel('bump\n(filtered)\n\n', ha='center')
m.ylim(-1.5, 1.5)

m.subplot(plots, 1, 2)
m.plot(t, filter(reader.sensors[:,2:4], 0.01))
m.ylabel('bumpf\n(filtered)\n\n', ha='center')
m.ylim(-1.5, 1.5)

m.subplot(plots, 1, 3)
m.plot(t, filter(reader.sensors[:,4:6], 0.01))
m.ylabel('position\n(filtered)\n\n', ha='center')
m.ylim(-1.5, 1.5)

m.subplot(plots, 1, 4)
m.plot(t, filter(reader.sensors[:,6:8], 0.01))
m.ylabel('vision\n(filtered)\n\n', ha='center')
m.ylim(-1.5, 1.5)

m.subplot(plots, 1, 5)
m.plot(t, filter(reader.correct, 0.05))
m.ylim(-1.5, 1.5)
m.ylabel('drive\n(training)\n\n', ha='center')


m.subplot(plots, 1, 6)
m.plot(reader.time, reader.drive)
m.ylim(-1.5, 1.5)
m.ylabel('drive\n(learned)\n\n', ha='center')
m.xlabel('time (s)')

#m.savefig('smart_view.png', dpi=900)
m.show()
"""