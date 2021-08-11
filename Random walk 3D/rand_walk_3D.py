"""3D random walk simulation using matplotlib."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random
from matplotlib.widgets import Slider

# setting axes limits so that graph axis stay the same during walk
limit_axis = 50
# starting coordinates
x0 = limit_axis/2
y0 = limit_axis/2
z0 = limit_axis/2

step_len = 2
step_options =  [[step_len,0,0],[-step_len,0,0],[0,-step_len,0],[0,step_len,0],[0,0,step_len],[0,0,-step_len]]

# holding x,z,y coordinates of ech step
xn = [x0]
yn = [y0]
zn = [z0]

txt_titel = "Step {}"
# producing steps
def stepChoice():
    # get direction of a new step
    choice = random.choice(step_options)
    # calculating new step and adding it
    xn.append(choice[0]+xn[-1])
    yn.append(choice[1]+yn[-1])
    zn.append(choice[2]+zn[-1])

# speed of animation
pause = [.5] 
def update_speed(val):
    pause[0] = 1.01-val


def handle_close(evt):
    global run 
    run = False

# vizualizing steps
def visualization(num_steps = 1000):
    global run 
    run = True
    # inicializing 3D plot
    fig = plt.figure("Random Walk")
    ax = fig.add_subplot(111, projection='3d')
        
    #Slider
    axamp = plt.axes([0.25, .03, .50, 0.02])
    samp = Slider(axamp, 'Speed', 0.01, 1, valinit=pause[0])

    while run:

        # calling stepChoice() to produce new step
        stepChoice()

        # actual ploting and changing titel
        ax.plot(xn,yn,zn)
        plt.title(txt_titel.format(len(xn)-1),fontdict=None, loc='right')

        # settign axes limits so that graph axis stay the same during walk
        ax.set_xlim (0,limit_axis)
        ax.set_ylim (0,limit_axis)
        ax.set_zlim (0,limit_axis)


        fig.canvas.mpl_connect('close_event', handle_close)

        # change speed of animation
        try:
            samp.on_changed(update_speed)
            plt.pause(pause[0])
        except:
            break

    plt.show()    

visualization()




