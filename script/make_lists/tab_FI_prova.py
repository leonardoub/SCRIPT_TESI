#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:32:51 2019

@author: leonardo
"""

import numpy as np
import json 
import pandas as pd

json_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.json'
bvec_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bvec'
bval_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bval'

with open(json_path) as json_file:
    A = json.load(json_file)


B = np.loadtxt(bvec_path)

C = np.loadtxt(bval_path) 

A.update({'bvec': B})
A.update({'bval': C})



TAB = pd.DataFrame.from_dict(A)
