import random
from itertools import count
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation  
import collections
import numpy as np
import time

#matplotlib.use('TkAgg')

x = collections.deque([1, 2, 3, 4, 5, 6], 5)
y = collections.deque([1, 2, 4, 0, 7, 3], 5) 
interval = 30
CHUNK = 5

# next is to make fig and axis of matplotlib plt
fig,ax = plt.subplots(figsize=(8,4))
# lets set the title
ax.set_title("PyShine")

plotdata = np.zeros((5, 1))
lines = ax.plot(plotdata, color=(0, 1, 0.29))

def update_plot(chunk):
    global plotdata

    while True:
        try:
            data = np.random.rand(CHUNK, 1)
        except Exception as e:
            print(e)
            break

        shift = len(data)
        plotdata = np.roll(plotdata, -shift,axis = 0)
        plotdata[-shift:,:] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:,column])
    return lines

ax.set_facecolor((0,0,0))
# Lets add the gr   id
ax.set_yticks([0])
ax.yaxis.grid(True)

ani  = FuncAnimation(fig,update_plot, interval=interval,blit=True)
plt.show()
