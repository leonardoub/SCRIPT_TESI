#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:52:50 2019

@author: leonardo
"""


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

A=['01','02','03','04','05','06','08','09','10','12','14','15','16','17','18','19','20','21','22','23','24','25','26','27']

mydict={k:0 for k in A}

for i in A:

    os.chdir('/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/')
    mask_list=os.listdir()

    mask_list.sort()
    mask_list2=[]

    for mask in mask_list:
        mask_name1=mask.replace('.nii.csv','')
        mask_name2=mask_name1.replace('_',' ')
        mask_name3=mask_name2.replace('mask','')
        mask_list2.append(mask_name3)
        
    if len(mask_list2)<48:
        mask_list2=mask_list2+(48-len(mask_list2))*['']
        

    mydict[i]=mask_list2

df=pd.DataFrame(mydict)   
    
df.to_csv('/home/leonardo/Scrivania/ROI_pazienti.csv')
