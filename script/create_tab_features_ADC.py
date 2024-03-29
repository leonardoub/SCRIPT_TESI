#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:32:24 2019

@author: leonardo
"""

import os
import glob
import pandas as pd



path_folder_with_csv='/home/leonardo/Scrivania/TESI/features/ADC_features/C_bc100'

file_list = os.listdir(path_folder_with_csv)

file_list.sort()

P = file_list[0]


A = glob.glob(path_folder_with_csv+'/*')
A.sort()


df = pd.read_csv(A[0])

dict_features = df.to_dict()


f_names=list(df.iloc[:,1])
f_value=list(df.iloc[:,2])

df_pat=pd.Series(data=f_value, index=f_names)