# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import json 
import pandas as pd
import os

path_list = '/home/leonardo/Scrivania/Tab_FI/pr.lst'

list_path = [line for line in open(path_list, 'r')]

D = {}

for i in range(len(list_path)):
      
    bval_path = list_path[i]
    json_path = bval_path.replace('.bval','.json')
    bvec_path = bval_path.replace('.bval','.bvec')
    name = json_path.split(os.sep)[-3][:-6]
   
    print(bval_path)
    print(bvec_path)
    print(json_path)
    print(name)
    
    with open(json_path) as json_file:
     print(json_path)
     print(json_file)
     A = json.load(json_file)

    interesting_keys = ['Manufacturer', 'ManufacturersModelName', 'ProtocolName']
    new_dict = {key : A[key] for key in interesting_keys}

    B = np.loadtxt(bvec_path)
    Bt = B.T
    sp = np.shape(Bt)[0]
    Bt_sp = np.vsplit(Bt, sp)
    dict_bvec = {f'Direzione {i} bvec': Bt_sp[i] for i in range(sp)}


    C = np.loadtxt(bval_path) 
    Ct = C.T
    dict_bval = {'bval' : Ct}

        
    dict_patient = {**new_dict, **dict_bvec, **dict_bval}
    
    bvec_keys = list(dict_bvec.keys())
    bval_keys = list(dict_bval.keys())

    D.update({name : dict_patient})


K=pd.DataFrame.from_dict(D, orient='index', columns=interesting_keys+bvec_keys+bval_keys)
