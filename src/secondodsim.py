import control
from matplotlib import pyplot as plt 
import numpy as np 

def simulate_system(z,w):
    sys = control.tf([w**2], [1, 2*z*w, w**2])
    print(f'\nsimulating with zeta={z}and Wn={w}')
    print('sys')

    t, y =control.step_response(sys)
    return t,y 

##case 1 underdamped (z<1)
t1 , y1 = simulate_system(z=0.5, w= 0.5)

plt.plot(t1,y1, label = 'Underdamped', linewidth=2)
plt.axhline(1.0, color='black', linestyle='--', label='target position')
plt.title("Step Response: Mass-Spring-Damper Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.legend()
plt.show()