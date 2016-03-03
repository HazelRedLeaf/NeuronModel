import math
import numpy as np
import matplotlib.pyplot as plt

def floatrange(x, y, step):
    while x < y:
        yield x
        x += step

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

# t represents each millisecond
for t in range(1, 1000):
    V.append(V[t - 1] + (E_l - V[t - 1] + R_m * I_e) / tau_m)
    if V[t] >= V_t:
        V[t] = V_r

# plot the results
plt.figure(0)
plt.plot(V)
plt.title('Integrate and fire neuron')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()
#############################################################


#############################################################
# Question 2.

I_e = (V_t - E_l) / R_m
print("I_e = ", I_e)

#############################################################


#############################################################
# Question 3.

I_e -= 0.1

# initialise empty array for all voltage values
V = []
V.append(V_r)

# t represents each millisecond
for t in range(1, 1000):
    V.append(V[t - 1] + (E_l - V[t - 1] + R_m * I_e) / tau_m)
    if V[t] >= V_t:
        V[t] = V_r

# plot the results
plt.figure(1)
plt.plot(V)
plt.title('Integrate and fire neuron 2')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()

#############################################################


#############################################################
# Question 4.

# initialise empty array for all spikes
spikes = []
I_e_s = []

for I_e in floatrange(2.0, 5.1, 0.1):
    I_e_s.append(I_e)

# i represents each input current
# t represents each millisecond
for I_e in floatrange(2.0, 5.1, 0.1):
    spikes.append(0)
    # initialise empty array for all voltage values
    V = []
    V.append(V_r)
    for t in range(1, 1000):
        V.append(V[t - 1] + (E_l - V[t - 1] + R_m * I_e) / tau_m)
        if V[t] >= V_t:
            V[t] = V_r
            spikes[-1] += 1

# plot the results
plt.figure(2)
plt.plot(I_e_s, spikes)
plt.title('Integrate and fire neuron 3')
plt.xlabel('Input current (nA)')
plt.ylabel('spikes (no.)')
plt.show()

#############################################################


#############################################################
# Question 5.

#############################################################


#############################################################
# Question 6.

#############################################################


#############################################################
# Question 7.

#############################################################