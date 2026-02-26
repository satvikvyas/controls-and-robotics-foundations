import numpy as np
import control as ct
import matplotlib.pyplot as plt


m = 1
d = 0.1
dt = 0.01

A= np.array(
    [[0,1],
     [0, -d/m]]
)

B= np.array(
    [[0],
     [1/m]]
)

q = np.array([
    [10,0],#position error weightage
    [0, 1]#velocity error weightage
])

#hehe
