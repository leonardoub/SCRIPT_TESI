#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:08:21 2019

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
    bvec_path = bval_path.replace('.bval','.bvec')
    name = bvec_path.split(os.sep)[-3][:-6]
    
    
    B = np.loadtxt(bvec_path)
    Bt = B.T
    sp = np.shape(Bt)[0]
    Bt_sp = np.vsplit(Bt, sp)
    dict_bvec = {f'Direzione {i} bvec': str(Bt_sp[i]).strip('[').strip(']') for i in range(sp)}
    
    
 
    bvec_keys = list(dict_bvec.keys())
        
        
    D.update({name : dict_bvec})
    
l=bvec_keys
K=pd.DataFrame.from_dict(D, orient='index', columns=l)


K.to_csv('/home/leonardo/Scrivania/Tab_FI/tab_bvec.csv', header=True)    
    
    
    
    
    