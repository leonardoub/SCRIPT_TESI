#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:12:23 2019

@author: leonardo
"""

import pandas as pd
import numpy as np
import os

A=['01','02']

os.chdir('/home/leonardo/Scrivania/Patients/87517/features_estratte')
mask_features_list=os.listdir()

for mask_features in mask_features_list:
    
mask_features_path='/home/leonardo/Scrivania/Patients/87517/RT_nii'+ mask_features    
 
df=pd.read_csv('/home/leonardo/Scrivania/Patients/93987/features_estratte/mask_encefalo.nii.csv', header='rows')




#c=df.iloc[43,1]