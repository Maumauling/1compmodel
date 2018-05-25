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
    '''Na current w. m, h channels; max.conduct. g_Na & reversal pot. E_Na'''
    return g_Na * np.power(m, 3) * h * (E_Na - V)


def I_K(n, V, g_K, E_K):
    ''' potassium current w. n channel; max.conduct. g_K & reversal pot. E_K'''
    return g_K * (np.power(n, 4)) * (E_K - V)


def I_leak(V, g_leak, E_leak):
    ''' leak current w. max. conduct. g_leak & reversal pot. E_leak'''
    return g_leak * (E_leak - V)


def I_syn(V, g_syn, E_syn):
    ''' synaptic current w. max. conduct. g_syn & reversal pot. E_syn'''
    return g_syn * (E_syn - V)
