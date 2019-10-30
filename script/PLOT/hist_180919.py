#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:06:20 2019

@author: leonardo
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt



table1=pd.read_csv('/home/leonardo/Scrivania/prove_180919/Pt_01_bW1.csv')
table2=pd.read_csv('/home/leonardo/Scrivania/prove_180919/Pt_01_bW01.csv')
table3=pd.read_csv('/home/leonardo/Scrivania/prove_180919/Pt_01_bW001.csv')

indici=[1,0.1,0.01]

features_list=[]

features_list.append(table1.iloc[62,2])
features_list.append(table2.iloc[62,2])
features_list.append(table3.iloc[62,2])




p=plt.bar(indici, features_list, color=(0.2, 0.4, 0.6, 0.6), linewidth=8)


