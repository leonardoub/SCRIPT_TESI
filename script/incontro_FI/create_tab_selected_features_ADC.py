#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:32:24 2019

@author: leonardo
"""

import os
import glob
import pandas as pd
import numpy as np


path = '/home/leonardo/Scrivania/ADC_features/C_bc100'

A = glob.glob(path+os.sep+'*')
A.sort()

interesting_features = ['original_firstorder_Minimum', 'original_firstorder_Maximum', 
                        'original_firstorder_MeanAbsoluteDeviation', 'original_firstorder_Mean', 
                        'original_firstorder_Median', 'original_firstorder_Range','original_firstorder_Variance']

D = {}

for i in A:
    
    patient = i.split(os.sep)[-1].replace('.csv', '')
    
    df = pd.read_csv(i)
    
    feature_names=list(df.iloc[:,1])
    feature_value=list(df.iloc[:,2])
    
    df_pat=pd.Series(data=feature_value, index=feature_names)
    
    dict_features=df_pat.to_dict()
    
    dict_selected_features = {key : dict_features[key] for key in interesting_features}

    D.update({patient : dict_selected_features})
    
    
    
D['Patient23']['original_firstorder_Minimum']='355.987'
D['Patient25']['original_firstorder_Minimum']='253.572'   

K=pd.DataFrame.from_dict(D, orient='index', columns=interesting_features)


K.to_csv('/home/leonardo/Scrivania/Tab_FI/tab_selected_features_ADC.csv', header=True)

#FARE PLOT

import matplotlib.pyplot as plt

pt_list=[pt.replace('Patient', '') for pt in K.index]
pt_list.sort()

min_=K.iloc[:,0]
list_min=list(min_)
min_np=min_.to_numpy(dtype=float)
plt.scatter(pt_list, min_np)


max_=K.iloc[:,1]
list_max=list(max_)
max_np=max_.to_numpy(dtype=float)
plt.scatter(pt_list, max_np, color='r')


plt.xticks(pt_list, rotation=90)
plt.yscale('log')
plt.ylim(10**0, 10**6)

for i in pt_list:
    plt.axvline(x=i, linestyle=':', color='k')

##########################################
##########################################
    
plt.show()

mean_=K.iloc[:,3]
mean_np=mean_.to_numpy(dtype=float)
#plt.scatter(pt_list, mean_np, color='r')

var=K.iloc[:,-1]
var_np=var.to_numpy(dtype=float)
stdv_np=np.sqrt(var_np)


plt.errorbar(pt_list, mean_np, yerr=stdv_np/2, fmt='.')
plt.xticks(pt_list, rotation=90)

############################################
############################################

plt.show()

plt.errorbar(pt_list, (max_np+min_np)/2, yerr=(max_np-min_np)/2, fmt='.')
plt.xticks(pt_list, rotation=90)

#for i,j in enumerate(pt_list):
#    plt.axvline(x=j, ymin=list_min[i], ymax=list_max[i])
#    plt.axvline(x=j, ymin=0.2, ymax=0.8)
#y=[78,65,98,32,100,50,64]
#
#plt.scatter(np.arange(len(y)), y)



#original_firstorder_Minimum
#
#original_firstorder_Maximum
#
#original_firstorder_MeanAbsoluteDeviation
#
#original_firstorder_Mean
#
#original_firstorder_Median
#
#original_firstorder_Range
#
#original_firstorder_Variance