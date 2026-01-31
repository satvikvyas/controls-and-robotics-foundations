#the perfect human knows how to code a dromne to float and stay at exactly 10 meters 
import numpy as np
import matplotlib.pyplot as plt
import control 


g = 9.81 #gravity
m = 1.0 #massdcc
dc = 0.1 #drag

dt= 0.01
tmax = 50 #the time limit
step = round(tmax/dt) 
time = np.linspace(0, tmax, step)


from pid import pidcontroller
d = pidcontroller(kp= 10, kd = 25 , ki = 0.7)
state = [0.0 , 0.0]
history = [] # the thing i will use to plot 
history_target =[]

for t in time :

    target = 10 + 5*np.sin(t)


    error = target - state[1]  #target position - actual position
    force = d.update(error , dt) 

    acc = force/m - g - (dc*state[0])/m
    state[0] += acc*dt #updating velocity
    state[1] += state[0]*dt #updating position 
    #so here index 0 is velocity and 1 is position, and thats the opposite of what i did in the pid smthg , so dont get confused

    history.append(state[1]) #state[1] for position
    history_target.append(target)
    #will run for for "time" then stop 

plt.plot(time , history , color = 'red', label = "actual path" )
plt.plot(time, history_target,color="black",  label = "the desired path")
plt.title('Drone with sine wave target')
plt.xlabel('Time (s)')
plt.ylabel('Position')
plt.grid(True)
plt.legend()
plt.show()

#tweaking the values of kp kd and ki 
#kd too high causes jittering
