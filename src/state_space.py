import numpy as np
import matplotlib.pyplot as plt

m= 1.0
d= 0.1
dt = 0.01

x_state = np.array( 
    [[0.0] , #position
     [0.0]] #velocity
)

#equation : x' = Ax + Bu
#for A(system matrix)

# [ 0 , 1 ]  -> position += velocity
# [ 0 , -d/m]  -> velocity += -drag

A = np.array(
    [[0,1],
     [0, -d/m]]
)

#for B()
# [ 0 ]   -> force doesn't change position directly
# [1/m]   -> force changes velocity (F=ma)

B= np.array(
    [[0],
    [1/m]]
)

history = []
time = np.linspace(0,10,1000)

for t in time :
    u = np.array([[10]])
    x = A @ x_state + B@u   # Ax+ Bu = xDOT
    x_state = x_state + x*dt
    history.append(x_state[0,0])

plt.plot(time , history)
plt.title("State Space Simulation (Matrix Form)")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid("true")    
plt.show()    

