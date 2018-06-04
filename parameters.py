#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:19:51 2018

@author: tiz
"""

# define needed global parameters, which won't be changed while testing
#%% import scheme

import numpy as np

#%% somatic conductances g for current dynamics I_Na, I_K, I_leak, I_syn
''' g_Na will be varied for testing active/passive soma, g_syn is described as
AC DC Input sinusoidal form, later on varied with amplitudes for left and 
right ear'''

g_K_som = 480 * 10**(-9)  # [mA / mV]
g_leak_som = 192 * 10**(-9)  # [mA / mV]
g_Na_som = 7 * 10**(-6)  # [mA / mV]
g_AC = 8 * 10**(-9)  # [mA / mV]
g_DC = 11.88 * 10**(-9)  # [mA / mV]
ampl_left = 1
ampl_right = 1


#%% reversal potentials
    
E_K = -75  # [mV]
E_leak = -65  # [mV]
E_Na = 50  # [mV]
E_syn = 0  # [mV]