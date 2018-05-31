#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:20:06 2018

@author: tiz
"""
#%% global import schemes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import integrate
from matplotlib.ticker import FormatStrFormatter


#%% needed functions and parameters import

from parameters import *
from currents import I_Na, I_K, I_leak, I_syn, mhnV
from gating_variables import alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h

#%% set local parameters

time_step = 0.01  # [ms]
t_range = np.arange(0, 500, time_step)  # [ms]
f = 0.004  # sound frequency
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
chann_data = pd.DataFrame(np.column_stack([t_range, sol[:,0:3]]), columns = ['time', 'm channel', 'h channel', 'n channel'])
curr_data = pd.DataFrame(np.column_stack([t_range, ina, ik, ileak, isyn]), columns = ['time', 'I_Na', 'I_K', 'I_leak', 'I_syn'])

volt_data.to_csv('membr_volt_1compmod.csv', index = False)
chann_data.to_csv('mhn_channels_1compmod.csv', index = False)
curr_data.to_csv('currents_1compmod.csv', index = False)

#'''PLOTSPECS'''
'''
fig = plt.figure(dpi=85)

gs = gridspec.GridSpec(8, 2)
gs.update(hspace=0.7)
ax1 = plt.subplot(gs[0:2, :])
ax2 = plt.subplot(gs[2:4, :])
ax3 = plt.subplot(gs[4:6, :])
ax4 = plt.subplot(gs[6:8, :])

ax1.plot(t_range, sol[:,3])
ax2.plot(t_range, sol[:,0], t_range, sol[:,1], t_range, sol[:,2])
ax3.plot(t_range, ina, t_range, ik, t_range, ileak)
ax4.plot(t_range, isyn)

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
ax1.set_ylabel('voltage []', size=10)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax2.set_ylabel('m,h,n \n channel', size=10)
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax3.set_ylabel('INa,IK,Ileak', size=10)
ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax3.set_xlabel('time [ms]', size=10)
'''