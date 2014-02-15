states='bvp'
N=1000

import stats
import syde556
from pylab import *
import numpy as np
import sys
sys.path.append('../ccmsuite')
import ccm
log = ccm.log()

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

types = []
for c in states:
    if c=='b': types.append('decoder_bumpout-filtered')
    if c=='v': types.append('decoder_vision')
    if c=='p': types.append('decoder_positionout')
    


state = np.hstack([reader[k] for k in types])
dimensions = state.shape[1]

target = reader.decoder_driveout

state = filter(state, 0.5)
target = filter(target, 0.5)


a = syde556.Ensemble(neurons=N, dimensions=dimensions)
#d = a.compute_decoder(state.T[:,:2000], target.T[:,:2000])
d = a.compute_decoder(state.T, target.T)

A, xhat = a.simulate_rate(state.T, d)

rmse = np.sqrt(np.mean((target-xhat.T)**2))
print rmse
log.rmse = rmse

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