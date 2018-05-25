#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:20:06 2018

@author: tiz
"""
#%% global import schemes

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import integrate


#%% needed functions and parameters import

from parameters import *
from currents import I_Na, I_K, I_leak, I_syn
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

def mhnV(y, t, C, f, g_Na, E_Na, g_K, E_K, g_leak, E_leak, g_syn, E_syn):
    ''' runge kutta workaround for system of 2 ODEs,
    define variables as y,
    dydt-vector includes righthandside of variable's ODE, callable for odeint'''
    m,h,n,V = y
    dmdt = 2*(alpha_m(V)*(1-m) - beta_m(V)*m)
    dhdt = 2*(alpha_h(V)*(1-h) - beta_h(V)*h)
    dndt = 2*(alpha_n(V)*(1-n) - beta_n(V)*n)
    dVdt = (1/C) * (I_Na(m,h, V,g_Na,E_Na) + I_K(n,V,g_K,E_K) + I_leak(V,g_leak,E_leak) + I_syn(V,g_syn,E_syn))
    return dmdt, dhdt, dndt, dVdt

sol = integrate.odeint(mhnV, [m0, h0, n0, V0], t_range, args = (C_som, f, g_Na_som, E_Na, g_K_som, E_K, g_leak_som, E_leak, g_syn_som(f,t_range, g_DC, g_AC, ampl_left, ampl_right, delta), E_syn) )