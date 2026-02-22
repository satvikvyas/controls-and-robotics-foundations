import numpy as np
import matplotlib.pyplot as plt

m= 1.0
d= 0.1
dt = 0.01

x_state = np.array( 
    [[0.0]  #position
     [0.0]] #velocity
)

#equation : x' = Ax + Bu
#for A(system matrix)

# [ 0 , 1 ]  -> position += velocity
# [ 0 , -d/m]  -> velocity += -drag

A = np.array(
    [[0,1]
     [0, -d/m]]
)

#for B()
# [ 0 ]   -> force doesn't change position directly
# [1/m]   -> force changes velocity (F=ma)

B= np.array(
    [[0]
    [1/m]]
)