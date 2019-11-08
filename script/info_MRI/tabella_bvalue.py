#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:13:01 2019

@author: leonardo
"""


import pandas as pd
import numpy as np



file_path_b_value = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient56_AIM56/Patient56_AIM56_MR_2018-01-18_104642_RM.ENCEFALO.MDC_DWI.HR_n423__00000/-a.bval'
file_path_b_vect = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient29_AIM29/Patient29_AIM29_MR_2014-11-06_132852_RM.ENCEFALO.MIDOLLO.MDC_DWI.HR_n175__00000/-a.bvec'    

b_value=np.loadtxt(file_path_b_value)
b_vect = np.loadtxt(file_path_b_vect)

df = pd.DataFrame({})