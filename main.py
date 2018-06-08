#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:20:06 2018

@author: tiz
"""
#%% global import schemes

import numpy as np
import pandas as pd
from scipy import integrate


#%% needed functions and parameters import

from parameters import *
from currents import I_Na, I_K, I_leak, I_syn, mhnV


#%% set local parameters

time_step = 0.01  # [ms]
t_range = np.arange(0, 50, time_step)  # [ms]
f = 0.2# sound frequency
delta = 0  # interaural phase difference
C_som = 24 * 10**(-12)  # [mA * s / mV]

#%% initialize ODE for solving membrane voltage

V0 = -65
m0 = .0529
h0 = .5961
n0 = .3177

sol = integrate.odeint(mhnV, [m0, h0, n0, V0], t_range, args = (C_som, g_Na_som, E_Na, g_K_som, E_K, g_leak_som, E_leak, g_DC, g_AC, f, delta, E_syn))

ina = I_Na(sol[:,0], sol[:,1], sol[:,3], g_Na_som, E_Na)
ik = I_K(sol[:,2], sol[:,3], g_K_som, E_K)
ileak = I_leak(sol[:,3], g_leak_som, E_leak)
isyn = I_syn(sol[:,3], t_range, g_DC, g_AC, f, delta, E_syn)

volt_data = pd.DataFrame(np.column_stack([t_range, sol[:,3]]), columns = ['time', 'memb_voltage'])
chann_data = pd.DataFrame(np.column_stack([t_range, sol[:,0:3]]), columns = ['time', 'm_channel', 'h_channel', 'n_channel'])
curr_data = pd.DataFrame(np.column_stack([t_range, ina, ik, ileak, isyn]), columns = ['time', 'I_Na', 'I_K', 'I_leak', 'I_syn'])

volt_data.to_csv('data/membr_volt_1compmod.csv', index = False)
chann_data.to_csv('data/mhn_channels_1compmod.csv', index = False)
curr_data.to_csv('data/currents_1compmod.csv', index = False)
