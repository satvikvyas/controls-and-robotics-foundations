import numpy as np
import control as ct
import matplotlib.pyplot as plt


dt = 0.01
m=1
d=0.1


A = np.array(
    [[0,dt],
     [0,1 - (d/m)*dt]])

B =  np.array([
    [0],
    [1/m]
])

H = np.array([[1,0]]) #because our ultrasonic sensor only measures position, not velocity

Q = np.diag([0.1,0.1]) #for processing noise 

R = np.array([[50.0]])  #our sensor is noisy


#creating "real" data
time =  np.arange(0 , 20, dt)
true_pos = 10 + 5*(np.sin(time))
noisy_sensor = np.array(np.random.normal(0,5.0))


xdot = np.array([
    [0],
    [0]]
)

P= np.identity(2)
x_state = np.array(
    [[0],
     [0]]
)
history_predicted =[]
history

for t in time:
    #for prediction equations

    u = np.array([[10]])
    x = A@x_state + B@u
    # history.append(x)
    x_state=x

    p = A@P@(np.transpose(A)) + Q
    P = p

    #for updating equation
    k= p@(np.transpose(H))*(np.linalg.inv(H@p@(np.transpose(H)) +R))
    xf = x + k@(noisy_sensor- H@x)


    history_predicted.append(xf[0])

