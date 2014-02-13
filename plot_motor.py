import stats
import numpy as np

reader = stats.Reader('SpinnMotor')

import math
def filter(data, tau, dt=0.001):
    decay = math.exp(-dt/tau)
    data = np.array(data)
    for i in range(len(data)-1):
        data[i+1] = data[i+1]*(1-decay)+data[i]*decay
    return data    


plot = stats.plot.time.Time(reader.time-1, border_left=1.2, border_bottom=0.6, time_range=(0,5))



plot.add('raw movement\ndirection', reader.input2, range=(-1.1, 1.1))
plot.add_spikes('neural\nactivity\n\n', reader.motor_spikes, cluster=False, merge=20, contrast_scale=0.5)
plot.add('decoded\nneural\nrepresentation', filter(reader.motor, 0.03), range=(-1.1, 1.1))
plot.save('motor.png', dpi=600)

plot.show()
