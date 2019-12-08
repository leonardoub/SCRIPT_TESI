#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:30:00 2019

@author: leonardo
"""
import numpy as np
import pandas as pd
import os



path_folder_with_csv='/home/leonardo/Scrivania/TESI/features/ADC_features/C_bc100/'

patient_list=os.listdir(path_folder_with_csv)

df_patient=[]

for patient in patient_list:
    df=pd.read_csv(path_folder_with_csv+patient)

    f_names=list(df.iloc[:,1])
    f_value=list(df.iloc[:,2])

    df_pat=pd.Series(data=f_value, index=f_names)
    
    df_patient.append(df_pat)


df1=pd.concat(df_patient, axis=1)

df2=df1.T

patient_list=[k.replace('.csv','') for k in patient_list]

df2.index=patient_list

#AGGIUNGERE LA COLONNA DEGLI OUTCOME
#caricare la colonna degli outcome

path_list_outcome='/home/leonardo/Scrivania/TESI/tabelle/list_for_classification.ods'

df_outcome=pd.read_excel(path_list_outcome, engine='odf')

names=list(df_outcome.iloc[:,0])
outcome_values=list(df_outcome.iloc[:,1])

df_pat_outcome=pd.Series(data=outcome_values, index=names)

df3=pd.concat([df2,df_pat_outcome], axis=1)

#df2.to_csv('/home/leonardo/Scrivania/TESI/tabella/tab.csv', sep='\t')

#DOVREBBE ANDAR BENE
df3.to_csv(r'/home/leonardo/Scrivania/TESI/tabelle/ADC/tab_outcome_C_bc_100_for_classification', header=True)
    







