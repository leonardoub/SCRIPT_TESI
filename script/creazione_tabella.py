#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:30:00 2019

@author: leonardo
"""
import numpy as np
import pandas as pd
import os

os.chdir('/home/leonardo/Scrivania/TESI/features_estratte_bW1')
patient_list=os.listdir()

df_patient=[]

for patient in patient_list:
    df=pd.read_csv('/home/leonardo/Scrivania/TESI/features_estratte/'+patient)

    f_names=list(df.iloc[:,1])
    f_value=list(df.iloc[:,2])

    df_pat=pd.Series(data=f_value, index=f_names)
    
    df_patient.append(df_pat)


df1=pd.concat(df_patient, axis=1)

df2=df1.T

patient_list=[k.replace('.csv','') for k in patient_list]

df2.index=patient_list



#df2.to_csv('/home/leonardo/Scrivania/TESI/tabella/tab.csv', sep='\t')

#DOVREBBE ANDAR BENE
df2.to_csv(r'/home/leonardo/Scrivania/TESI/tabella/tab_bW1.csv', header=True)
    







