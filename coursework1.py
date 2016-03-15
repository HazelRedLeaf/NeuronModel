import math
import numpy as np
import random
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
plt.title('Integrate and fire neuron model')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()
#############################################################


#############################################################
# Question 2.

I_e = (V_t - E_l) / R_m
print("I_e_min = ", I_e) #to add nA

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
plt.title('Integrate and fire neuron model')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()

#############################################################


#############################################################
# Question 4.

# initialise empty array for all spikes
spikes = []
I_e_s = []

for I_e in floatrange(2.0, 5.0, 0.1):
    I_e_s.append(I_e)

# i represents each input current
# t represents each millisecond
for I_e in floatrange(2.0, 5.0, 0.1):
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
plt.title('Firing rate of neurons')
plt.xlabel('Input current (nA)')
plt.ylabel('spikes (no.)')
plt.show()

#############################################################


#############################################################
# Question 5.

#############################################################
# variables                                                 #
#                                                           #
# tau_m = 20 ms         - membrane time constant            #
# E_l = -70 mV          - leak potential                    #
# V_r = -80 mV          - reset voltage                     #
# V_t = -54 mV          - threshold                         #
# R_m * I_e = 18 mV     - resitance * current               #
#                                                           #
# Synapses                                                  #
# R_m * g_s = 0.15                                          #
# P = 0.5                                                   #
# tau_s = 10 ms                                             #
# a) E_s = 0 mV                                             #
# b) E_s = -80 mV                                           #
#############################################################
tau_m = 20
E_l = -70
V_r = -80
V_t = -54
R_m_I_e = 18
R_m_g_s = 0.15
P = 0.5
tau_s = 10

# a)
E_s = 0

# initialise empty array for all voltage values
V_1 = []
v_1 = random.uniform(V_r, V_t)
V_1.append(v_1)
t_1 = 0
V_2 = []
v_2 = random.uniform(V_r, V_t)
V_2.append(v_2)
t_2 = 0

# t represents each millisecond
for t in range(1, 1000):
    V_1.append(V_1[-1] + (E_l + R_m_I_e - V_1[-1] - R_m_g_s * P * math.exp(- (t - t_2) / tau_s) * (V_1[-1] - E_s)) / tau_m)
    if V_1[-1] >= V_t:
        V_1[-1] = V_r
        t_1 = t + 1
    V_2.append(V_2[-1] + (E_l + R_m_I_e - V_2[-1] - R_m_g_s * P * math.exp(- (t - t_1) / tau_s) * (V_2[-1] - E_s)) / tau_m)
    if V_2[-1] >= V_t:
        V_2[-1] = V_r
        t_2 = t + 1

# plot the results
plt.figure(3)
plt1, = plt.plot(V_1, color = 'r')
plt2, = plt.plot(V_2, color = 'b')
plt.title('Interprojection of two neurons (excitatory synapses)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()


# b)
E_s = -80

# initialise empty array for all voltage values
V_1 = []
v_1 = random.uniform(V_r, V_t)
#v_1 = -80
V_1.append(v_1)
t_1 = 0
V_2 = []
v_2 = random.uniform(V_r, V_t)
#v_2 = -79
V_2.append(v_2)
t_2 = 0

# t represents each millisecond
for t in range(1, 1000):
    V_1.append(V_1[-1] + (E_l + R_m_I_e - V_1[-1] - R_m_g_s * P * math.exp(- (t - t_2) / tau_s) * (V_1[-1] - E_s)) / tau_m)
    if V_1[-1] >= V_t:
        V_1[-1] = V_r
        t_1 = t + 1
    V_2.append(V_2[-1] + (E_l + R_m_I_e - V_2[-1] - R_m_g_s * P * math.exp(- (t - t_1) / tau_s) * (V_2[-1] - E_s)) / tau_m)
    if V_2[-1] >= V_t:
        V_2[-1] = V_r
        t_2 = t + 1

# plot the results
plt.figure(4)
plt1, = plt.plot(V_1, color = 'r')
plt2, = plt.plot(V_2, color = 'b')
plt.title('Interprojection of two neurons (inhibitory synapses)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()

#############################################################


#############################################################
# Question 6.

#############################################################
# variables                                                 #
#                                                           #
# tau_m = 10 ms         - membrane time constant            #
# E_l = V_r = -70 mV    - leak potential = reset voltage    #
# V_t = -40 mV          - threshold                         #
# R_m = 10 MOmega       - resitance                         #
# I_e = 3.1 nA          - current                           #
# E_k = -80 mV          - reversal potential                #
# dR = 0.005 MOmega-1   - conductance increase              #
# tau = 200 ms          - time constant                     #
# dt = 1 ms             - for 1 second                      #
#############################################################

tau_m = 10
V_r = -70
V_t = -40
R_m = 10.
I_e = 3.1
E_k = -80.
E_l = -70.
G_m = 0
tau = 200.

# initialise empty array for all voltage values
V = []
V.append(V_r)

# t represents each millisecond
for t in range(1, 1000):
    V.append(V[-1] + (E_l - V[-1] + (R_m * I_e) + R_m * G_m * (E_k - V[-1])) / tau_m)
    G_m -= G_m / tau
    if V[-1] > V_t:
        V[-1] = V_r
        G_m += 0.0005

# plot the results
plt.figure(5)
plt.plot(V)
plt.title('Integrate and fire neuron with a potassium current')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()

#############################################################


#############################################################
# Question 7.

#############################################################