"""1D Rand Walk vizualization (1. plot) and statistics (2. plot)."""

import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

curr_pos = 0

x_axis = np.arange(-10, 11, 1)
x_values = np.arange(-10,11,1)

xy_bar = dict()

len_walk = 10
xn = []
yn = []

txt_subplot1 = "Turns {}"
txt_subplot2 = "Walks {}"

walks = 0

#pause
pause = [.5] #!
def update_speed(val):
    pause[0] = 1.0001-val

# 2 functions for vizualization
def viz_subplot1(curr_pos,marker,iteration):
    if step == 1:
        marker = 'r>'
    else:
        marker = 'b<'

    axs[0].plot(curr_pos,0.2, marker,linewidth=2, markersize=10)

    axs[0].grid() # grid on
    
    axs[0].set_title('Random Walk')

    #axs[0].set_title('subplot 1')
    axs[0].set_title(txt_subplot1.format(iteration+1),fontdict=None, loc='right')
    axs[0].set_xlabel('Distance')

    # setting axes limits so that graph axis dont change during walk
    axs[0].set_xlim (-10,10)
    axs[0].set_ylim (0,1)
    
    # so that closing dont cause exeption
    try:
        plt.pause(pause[0])
    except:
        pass

    axs[0].cla()

def viz_subplot2(curr_pos,num_games):

    if curr_pos in xy_bar:
        xy_bar[curr_pos] = xy_bar[curr_pos] + 1
    else:
        xy_bar[curr_pos] = 1

    for x, y in xy_bar.items():
        xn.append(x)
        yn.append(y)

    axs[1].bar(xn,yn)
    axs[1].set_title(txt_subplot2.format(walks),fontdict=None, loc='right')
    axs[1].set_xlim (-10,10)
    
def handle_close(evt):
    global run 
    run = False

# Main
fig, axs = plt.subplots(2, 1, constrained_layout=False)
plt.xticks(np.arange(-10, 11, 1))

#Slider
axamp = plt.axes([0.25, .03, .40, 0.02])
samp = Slider(axamp, 'Speed',0,1, valinit=pause[0])

global run 
run = True

while run:

    for iteration in range (len_walk):
        step = random.choice([1,-1])
        curr_pos += step

        if step == 1:
            marker = 'r>'
        else:
            marker = 'b<'

        samp.on_changed(update_speed) # changing speed
        viz_subplot1(curr_pos, marker,iteration)

        fig.canvas.mpl_connect('close_event', handle_close)

        if iteration == 9:
            walks += 1
            
    viz_subplot2(curr_pos, walks )

    curr_pos = 0
    xn = []
    yn = []

plt.show()
