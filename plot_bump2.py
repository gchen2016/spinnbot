import stats
import numpy as np

reader = stats.Reader('FilteredSpinnBump')

import math
def filter(data, tau, dt=0.001):
    decay = math.exp(-dt/tau)
    data = np.array(data)
    for i in range(len(data)-1):
        data[i+1] = data[i+1]*(1-decay)+data[i]*decay
    return data    


plot = stats.plot.time.Time(reader.time, border_left=1.2, border_bottom=0.6)

plot.add('raw bump\nsensors', reader.input2)
plot.add_spikes('neural\nactivity\n\n', reader.bump_spikes, cluster=False, sample=40, contrast_scale=0.5)
plot.add('decoded\nneural\nrepresentation', filter(reader.bump, 0.03))
plot.save('bump_filtered.png', dpi=600)
plot.show()
