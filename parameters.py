#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:19:51 2018

@author: tiz
"""

# define needed global parameters, which won't be changed while testing

#%% conductances g for current dynamics I_Na, I_K, I_leak, I_syn
''' g_Na will be varied for testing active/passive soma, g_syn is described as
AC DC Input sinusoidal form, later on varied with amplitudes for left and 
right ear'''

g_K_som = 480 * 10**(-9)  # [g_K_som] = mA / mV
g_leak_som = 192 * 10**(-9)  # [g_leak_som] = mA / mV
# g_Na: range modified in main


def g_syn(f,t):
    ''' synaptic input modelled via conductance, AC and DC input parts, 
    where only AC is ITD dependent,
    [g_syn] = mA / mV'''
    return 