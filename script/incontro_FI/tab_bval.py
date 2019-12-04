#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:06:32 2019

@author: leonardo
"""


import numpy as np
import pandas as pd
import os


path_list = '/home/leonardo/Scrivania/Tab_FI/pr.lst'
#path_list = '/home/leonardo/Scrivania/Tab_FI/tab_pr.lst'


list_path = [line.strip('\n') for line in open(path_list, 'r')]

list_path.sort()

D = {}

for i in range(len(list_path)):
      
    bval_path = list_path[i]
    name = bval_path.split(os.sep)[-3][:-6]
    
    
    C = np.loadtxt(bval_path) 
    Ct = C.T
    dict_bval = {'bval' : str(Ct).strip('[').strip(']')}
    
    bval_keys = list(dict_bval.keys())

    D.update({name : dict_bval})

l=bval_keys
K=pd.DataFrame.from_dict(D, orient='index', columns=l)


K.to_csv('/home/leonardo/Scrivania/Tab_FI/tab_bval.csv', header=True)



    
