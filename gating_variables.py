#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:37:06 2018

@author: tiz
"""
#%% defined params
eps = 10**(-12)

#%% potassium (K) gating variable n

def alpha_n(V):
    ''' K gating variable n dynamics,
    including exception for div. by zero,
    solved with l'hospital'''
    if abs(V + 55) < eps:
        return .1
    return (.01 * (V+55)) / (1 - np.exp(-.1 * (V+55))) 
    

def beta_n(V):
    ''' K gating variable n dynamics,'''
    return .125 * np.exp(-.0125 * (V+65))
    
#%% sodium (Na) gating variables m and h


def alpha_m(V):
    ''' sodium m channel voltage dependent transition rate'''
    if abs(V + 40) < eps:
        return 1.0
    return (.1 * (V+40)) / (1 - np.exp(-.1 * (V+40)))


def alpha_h(V):
    ''' sodium h channel voltage dependent transition rate'''
    return .07 * np.exp(-.05 * (V+65))


def beta_m(V):
    ''' sodium m channel voltage dependent transition rate'''
    return 4 * np.exp(-.0556 * (V+65))


def beta_h(V):
    ''' sodium h channel voltage dependent transition rate'''
    if abs(V + 35) < eps:
        return .5
    return 1 / (1 + np.exp(-.1 * (V+35)))
