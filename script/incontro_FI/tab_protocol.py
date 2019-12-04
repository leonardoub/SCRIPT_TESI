#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:38:37 2019

@author: leonardo
"""


import numpy as np
import json 
import pandas as pd
import os

path_list = '/home/leonardo/Scrivania/Tab_FI/pr.lst'
#path_list = '/home/leonardo/Scrivania/Tab_FI/tab_pr.lst'

list_path = [line.strip('\n') for line in open(path_list, 'r')]

list_path.sort()
D = {}

for i in range(len(list_path)):
      
    bval_path = list_path[i]
    json_path = bval_path.replace('.bval','.json')
    name = json_path.split(os.sep)[-3][:-6]
    
    with open(json_path) as json_file:
        A = json.load(json_file)

    interesting_keys = ['Manufacturer', 'ManufacturersModelName', 'ProtocolName', 'SeriesDescription', 'SliceThickness', 'SpacingBetweenSlices']
    new_dict = {key : A[key] for key in interesting_keys}
        
    D.update({name : new_dict})
    
    
K=pd.DataFrame.from_dict(D, orient='index', columns=interesting_keys)

K.to_csv('/home/leonardo/Scrivania/Tab_FI/tab_protocol.csv', header=True)

