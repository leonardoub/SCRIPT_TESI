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

A=['01','02','03','04','05','06','08','09','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']

#L=['04']
#
#for j in A:
#    os.mkdir('/home/leonardo/Scrivania/Patients/'+j+'/plot/hist/features_quadratiche/')
    


for i in A:
    os.chdir('/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/')
    mask_features_list=os.listdir()
    
    for mask_features in mask_features_list:
    
            mask_features_path='/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/'+ mask_features    
     
            df=pd.read_csv(mask_features_path)
            
            FO_names=list(df.iloc[46:64,1])
            FO_features=df.iloc[46:64,2]
            FO_features_list=FO_features.tolist()
            
            FO_features_list_fl=[float(j) for j in FO_features_list]
            FO_features_list_fl.pop(17)
            FO_features_list_fl.pop(16)
            FO_features_list_fl.pop(14)
            FO_features_list_fl.pop(13)
            FO_features_list_fl.pop(12)
            FO_features_list_fl.pop(11)
            FO_features_list_fl.pop(10)
            FO_features_list_fl.pop(9)
            FO_features_list_fl.pop(8)
            FO_features_list_fl.pop(7)
            FO_features_list_fl.pop(6)
            FO_features_list_fl.pop(5)
            FO_features_list_fl.pop(4)
            FO_features_list_fl.pop(3)
            FO_features_list_fl.pop(1)             
            FO_features_list_fl.pop(0)             
            
#            
#            Max=max(FO_features_list_fl)
#            Min=min(FO_features_list_fl)
#            
            FO_names=[k.replace('original_firstorder_','') for k in FO_names]
            FO_names.pop(17)
            FO_names.pop(16)
            FO_names.pop(14)
            FO_names.pop(13)
            FO_names.pop(12)
            FO_names.pop(11)
            FO_names.pop(10)
            FO_names.pop(9)
            FO_names.pop(8)
            FO_names.pop(7)
            FO_names.pop(6)
            FO_names.pop(5)
            FO_names.pop(4)
            FO_names.pop(3)
            FO_names.pop(1)             
            FO_names.pop(0)
            
            N=len(FO_names)
            
            indici=np.arange(N)
            width=0.05
            
            p=plt.bar(indici, FO_features_list_fl, width, color=(0.2, 0.4, 0.6, 0.6))
            
#            plt.hist(FO_features_list_fl,indici-0.5)
            
            plt.xticks(indici, FO_names, rotation='vertical')
#            plt.yticks(np.arange(Min,Max,5))
            plt.ylabel('Dosex\u00b2 [Gyx\u00b2]')
            plt.title('Features quadratiche')
    
    
            plt.savefig('/home/leonardo/Scrivania/Patients/'+i+'/plot/hist/features_quadratiche/plot_features_lineari_'+mask_features+'.pdf',  bbox_inches = "tight")
            plt.close()  
            
            
            
#funziona soltanto che energia ed entropia sono fuori scala, le tolgo?
#NON lineari: Energy, Total Energy            
            
#adimensionali: Entropy? sì, Skewness, Kurtosis, Uniformity? sì, Interquartile Range          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            