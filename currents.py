#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:21:06 2018

@author: tiz
"""
#%% import schemes

import numpy as np

#%% dynamics for needed currents: Na, K, leak, synaptic

def I_Na(m, h, V, g_Na, E_Na):
    '''Na current w. m, h channels;
    max.conduct. g_Na & reversal pot. E_Na
    [I_Na] = mA'''
    return g_Na * np.power(m, 3) * h * (E_Na - V)


def I_K(n, V, g_K, E_K):
    ''' potassium current w. n channel;
    max.conduct. g_K & reversal pot. E_K
    [I_K] = mA'''
    return g_K * (np.power(n, 4)) * (E_K - V)


def I_leak(V, g_leak, E_leak):
    '''leak current w. max. conduct. g_leak & reversal pot. E_leak
    [I_leak] = mA'''
    return g_leak * (E_leak - V)


def I_syn(V, t, g_DC, g_AC, f, delta, E_syn):
    ''' synaptic current w. max. conduct. g_syn & reversal pot. E_syn
    [I_syn] = mA'''
    return (g_DC + g_AC *(np.sin(2*np.pi*f*t)+np.sin(2*np.pi*f*t+delta))) * (E_syn - V)

#%% solution workaround for ODEs describing membrane voltage
    
def mhnV(y, t, C, g_Na, E_Na, g_K, E_K, g_leak, E_leak, g_DC, g_AC, f, delta, E_syn):
    ''' runge kutta workaround for system of 4 ODEs,
    define variables as y,
    dydt-vector includes righthandside of variable's ODE, callable for odeint'''
    m,h,n,V = y
    dmdt = 2*(alpha_m(V)*(1-m) - beta_m(V)*m)
    dhdt = 2*(alpha_h(V)*(1-h) - beta_h(V)*h)
    dndt = 2*(alpha_n(V)*(1-n) - beta_n(V)*n)
    dVdt = (1/C) * (I_Na(m,h, V,g_Na,E_Na) + I_K(n,V,g_K,E_K) + I_leak(V,g_leak,E_leak) + I_syn(V, t, g_DC, g_AC, f, delta, E_syn))
    return dmdt, dhdt, dndt, dVdt

#%% synaptic somatic conductance (not explicitly used, might be useful)
    
def g_syn_som(f,t, g_DC, g_AC, ampl_left, ampl_right, delta):
    ''' synaptic input modelled via conductance, AC and DC input conduct.,
    where only AC is ITD-dependent,
    f = sound freq., delta = interaural sound phase difference
    added amplitudes for left and right ear input strength
    [g_syn] = mA / mV'''
    return g_DC + g_AC * (ampl_left * np.sin(2*np.pi*f*t) + ampl_right*np.sin(2*np.pi*f*t + delta))

