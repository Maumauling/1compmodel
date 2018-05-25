#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:37:06 2018

@author: tiz
"""
#%% import scheme
import numpy as np

#%% defined params and import schemes
eps = 10**(-12)  # for determining division by zero limes

#%% potassium (K) gating variable n


def alpha_n(V):
    ''' K gating variable n dynamics,
    including exception for div. by zero,
    solved with l'hospital'''
    if abs(V + 60) < eps:
        return .1
    return (.01 * (V+60)) / (1 - np.exp(-.1 * (V+60)))


def beta_n(V):
    ''' K gating variable n dynamics'''
    return .125 * np.exp(-.0125 * (V+70))

#%% sodium (Na) gating variables m and h


def alpha_m(V):
    '''Na gating variable m dynamics,
    including exception for div. by zero,
    solved with l'hospital'''
    if abs(V + 45) < eps:
        return 1.0
    return (.1 * (V+45)) / (1 - np.exp(-.1 * (V+45)))


def alpha_h(V):
    '''Na gating variable h dynamics'''
    return .07 * np.exp(-.05 * (V+70))


def beta_m(V):
    '''Na gating variable m dynamics'''
    return 4 * np.exp(-(V+70)/18)


def beta_h(V):
    '''Na gating variable h dynamics'''
    return 1 / (1 + np.exp(-.1 * (V+40)))
