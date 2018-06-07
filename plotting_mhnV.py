#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:04:26 2018

@author: Tizia Kaplan

plotting routine for data generated via 1compmodel; mhnV runge kutta solution

wanted structure: if channelplotting = True -> in plot also channel kinetics, but can be only membrane voltage and so on. 

proposed structure:
    first define boolean variables for how much in plot included
    second go into if loop
    
    maybe beforehand plotting fcts need to be defined
    
"""
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import seaborn as sns
sns.set()


volt = True
chann = True
curr = True
isyn = True
save_fig = False

num_axes = sum([volt, chann, curr, isyn])
num_axes

if volt:
    voltage = pd.read_csv('data/membr_volt_1compmod.csv')
    
if chann:
    channels = pd.read_csv('data/mhn_channels_1compmod.csv')

if curr or isyn:
    currents = pd.read_csv('data/currents_1compmod.csv')
    
fig = plt.figure(dpi=100)

gs = gridspec.GridSpec(2*num_axes, 1)
for ax_idx, row_start, row_stop in zip(range(1,num_axes+1), range(0, num_axes*2, 2), range(2, num_axes*2 +2, 2)):
    exec('ax' + str(ax_idx) + '=' + 'plt.subplot(gs[row_start:row_stop,:])')

if volt:
    voltage = pd.read_csv('data/membr_volt_1compmod.csv')
    ax1.plot(voltage['time'], voltage['memb_voltage'])
    ax1.set_ylabel('voltage [mV]', size=10)
    plt.setp(ax1.get_xticklabels(), visible=False)

if chann:
    channels = pd.read_csv('data/mhn_channels_1compmod.csv')
    ax2.plot(channels['time'], channels['m_channel'], channels['time'], channels['h_channel'], channels['time'], channels['n_channel'])
    ax2.set_ylabel('m, h, n\nchannel', size=10)
    plt.setp(ax2.get_xticklabels(), visible=False)

if curr:
    currents = pd.read_csv('data/currents_1compmod.csv')
    ax3.plot(currents['time'], currents['I_Na'], currents['time'], currents['I_K'], currents['time'], currents['I_leak'])
    ax3.set_ylabel('I.Na, I.K,\nI.leak [mA]', size=10)
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    plt.setp(ax3.get_xticklabels(), visible=False)
    
if isyn:
    currents = pd.read_csv('data/currents_1compmod.csv')
    ax4.plot(currents['time'], currents['I_syn'])
    ax4.set_ylabel('I_synaptic\n[mA]', size=10)
    ax4.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    ax4.set_xlabel('time [ms]', size=10)
    
if save_fig:
    file_name = input("File Name?")
    fig.savefig('data/{}.pdf'.format(file_name))
    
#%% PLOT SPECS
'''
fig = plt.figure(dpi=85)

gs = gridspec.GridSpec(8, 1)
gs.update(hspace=2)
ax1 = plt.subplot(gs[0:2, :])
ax2 = plt.subplot(gs[2:4, :])
ax3 = plt.subplot(gs[4:6, :])
ax4 = plt.subplot(gs[6:8, :])

ax1.plot(voltage['time'], voltage['memb_voltage'])

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