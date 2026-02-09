import matplotlib.pyplot as plt
import numpy as np
from pid import pidcontroller as pid

g=9.81
m= 1.0
dc= 0.1
dt = 0.01
 
#now to define points where we need to make the drone go 
targets = [[0,0], [0,10], [15,10], [20, 25]]
idx = 1 # the first index so it goes to 0,10
tolerance = 0.3

pidx = pid(kp=2, kd = 5 , ki = 0.5)
pidy = pid(kp=2, kd = 5 , ki = 0.5)

x , vx , y, vy = 0,0,0,0 # positions and velocities

historyx = []
historyy = []

while idx < len(targets):
    target = targets[idx]
    t_x, t_y = target[0], target[1]

    errorx = t_x - x
    errory = t_y - y

    forcex = pidx.update(errorx, dt)
    accx = forcex/m - (vx*dc)/m 
    
    forcey = pidy.update(errory, dt)
    accy = forcey/m - (m*g +  vx*dc)/m

    vx += accx*dt
    vy += accy*dt

    x += vx*dt
    y += vy*dt

    dist = ((t_x - x)**2 + (t_y - y)**2)**0.5
    speed = (vx**2 + vy**2)**0.5

    if dist< tolerance and speed < 0.5:
        print("target reached :3")
        idx +=1

    historyx.append(x)
    historyy.append(y)
    
    # Safety break
    if len(historyx) > 5000: 
        print("timeout")
        break

ix = [t[0] for t in targets]
iy = [t[1] for t in targets]

plt.figure(figsize= (8,8))
plt.plot(ix , iy , "ro", label = "targets")
plt.plot(historyx, historyy, label = "drone path")
plt.xlabel("x")
plt.ylabel("y")
plt.grid("true")
plt.legend()
plt.show()