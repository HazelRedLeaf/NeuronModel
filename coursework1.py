import math
import numpy as np
import matplotlib.pyplot as plt

#############################################################
# variables                                                 #
#                                                           #
# tau_m = 10ms          - membrane time constant            #
# E_l = V_r = -70 mV    - leak potential = reset voltage    #
# V_t = -40 mV          - threshold                         #
# R_m = 10 MOmega       - resitance                         #
# I_e = 3.1 nA          - current                           #
#                                                           #
# dt = 1 ms             - for 1 second                      #
#############################################################
tau_m = 10
E_l = V_r = -70
V_t = -40
R_m = 10
I_e = 3.1


#############################################################
# Question 1.

# initialise empty array for all voltage values
V = []
V.append(V_r)

# i represents each millisecond
for t in range(1, 1000):
    V.append(V[t - 1] + (E_l - V[t - 1] + R_m * I_e) / tau_m)
    if V[t] >= V_t:
        V[t] = V_r

# plot the results
plt.plot(V)
plt.title('Integrate and fire neuron')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()