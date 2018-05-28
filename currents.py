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
