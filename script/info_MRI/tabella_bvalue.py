#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:13:01 2019

@author: leonardo
"""


import pandas as pd
import numpy as np



file_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient56_AIM56/Patient56_AIM56_MR_2018-01-18_104642_RM.ENCEFALO.MDC_DWI.HR_n423__00000/-a.bval'
    
b_value=np.loadtxt(file_path)

df = pd.DataFrame({})