#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:20:19 2019

@author: leonardo
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

A=['03','04','05','06','08','09','10','12','14','15','16','17','18','19','20','21','23','24','25','26','27']

#L=['04']
#
#for j in A:
#    os.mkdir('/home/leonardo/Scrivania/Patients/'+j+'/plot/hist/features_adimensionali/')
    
feature_list=[]

name_list2=[]

for i in A:
    os.chdir('/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/')
    
    
    mask_features_path='/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/mask_ polmone dx.nii.csv'   
     
    df=pd.read_csv(mask_features_path)
            
    name_list=list(df.iloc[:,1])
    
    ind=name_list.index('original_firstorder_Kurtosis')
    
    
    
    
    feature=float(df.iloc[ind,2])
 
    name=name_list[ind]
      
#            
#            Max=max(FO_features_list_fl)
#            Min=min(FO_features_list_fl)
#            
    name1=name.replace('original_firstorder_','')

    name_list2.append(name1)
    
    feature_list.append(feature)

N=len(A)        
            
indici=np.arange(N)
width=0.5
            
p=plt.bar(indici, feature_list, width, color=(0.2, 0.4, 0.6, 0.6))
            
#            plt.hist(FO_features_list_fl,indici-0.5)
            
plt.xticks(indici, A, rotation='vertical')
#            plt.yticks(np.arange(Min,Max,5))
#            plt.ylabel('Dose\u00b2 [Gy\u00b2]')
plt.title('Kurtosis')
    
    
plt.savefig('/home/leonardo/Scrivania/Patients/Kurtosis.pdf',  bbox_inches = "tight")
plt.close()  
            
            
            
#funziona soltanto che energia ed entropia sono fuori scala, le tolgo?
#NON lineari: Energy, Total Energy            
            
#adimensionali: Entropy? sì, Skewness, Kurtosis, Uniformity? sì, Interquartile Range          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            