import stats
import syde556
from pylab import *
import numpy as np

import math
def filter(data, tau, dt=0.01):
    decay = math.exp(-dt/tau)
    data = np.array(data)
    for i in range(len(data)-1):
        data[i+1] = data[i+1]*(1-decay)+data[i]*decay
    return data    


    
#reader = stats.Reader('SpinnSmartLR-20131207-072641')
#reader = stats.Reader('SpinnSmartLR-20131207-072826')
reader = stats.Reader('SpinnSmartLR-20131207-073020')

#reader = stats.Reader('SpinnSmart-20131207-071859')
#reader = stats.Reader('SpinnSmart-20131207-072050')
#reader = stats.Reader('SpinnSmart-20131207-072246')
#reader = stats.Reader('SpinnSmart-20131207-072423')

##reader = stats.Reader('SpinnSmartRetina2-20131207-084027')
##reader = stats.Reader('SpinnSmartRetina2-20131207-084238')
#reader = stats.Reader('SpinnSmartRetina2-20131207-084413')


state = np.hstack([
    reader['decoder_bumpout-filtered'],
    #reader['decoder_bumpout'],
    reader['decoder_vision'],
    reader['decoder_positionout'],
    ])
print state.shape  

target = reader.decoder_driveout

state = filter(state, 0.5)
target = filter(target, 0.5)



#for i in range(100):
if True:
    i=55
    a = syde556.Ensemble(neurons=1000, dimensions=6, seed=i)
    d = a.compute_decoder(state.T[:,:2000], target.T[:,:2000])
    #d = a.compute_decoder(state.T, target.T)

    A, xhat = a.simulate_rate(state.T, d)

    print i, min(xhat[1])

A, xhat2 = a.simulate_spikes(state.T, d, tau=0.1)

rmse = np.sqrt(np.mean((target-xhat.T)**2))
print rmse

plot = stats.plot.Time(reader.time, border_left=1.2)
plot.add('motor\ntraining\ndata', target, range=(-1.2, 1.2))
plot.add('sensor\nstate', state, range=(-1.2, 1.2))
plot.add_spikes('neural\nactivity\n\n', A, sample=100, cluster=False, merge=20, contrast_scale=0.5)
plot.add('decoded\nneural\nactivity', xhat.T, range=(-1.2, 1.2))
plot.save('lr.png', dpi=600)
plot.show()


#subplot(2,1,1)
#plot(reader.time, target)
#subplot(2,1,2)
#plot(reader.time, xhat.T)
#show()


#plot(reader.time, reader.control_drive_0)
#plot(reader.time, filter(reader.decoder_driveout, 0.1))
#plot(reader.time, filter(reader.decoder_bumpout, 0.1))
#plot(reader.time, filter(reader['decoder_bumpout-filtered'], 0.1))
#plot(reader.time, filter(reader.decoder_vision, 0.1))
#plot(reader.time, filter(reader.decoder_positionout, 0.1))
#show()
#state =

#decoder_driveout,decoder_bumpout,decoder_bumpout-filtered,decoder_vision,decoder_positionout