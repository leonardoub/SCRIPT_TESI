#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:41:11 2019

@author: leonardo
"""

import pandas as pd 
import shutil
import os

path_table_info_DWI = '/home/leonardo/Scrivania/TESI/tabelle_MRI/estratte_da_me/DWI/export_info_RM_DWI_pre.xlsx'
path_file_RM = '/media/leonardo/Dell_HD/RM_Patients_Anon'
output_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI'

table_DWI = pd.read_excel(path_table_info_DWI)

name_DWI = list(table_DWI['Percorso_RM'])

for name in name_DWI:
    
#    try:
        
    patient_name = name[:15]
    date = name[19 : 26]

#        os.chdir(f'{output_path}')
#        os.makedirs(f'{patient_name}/{date}__Studies')
#        
    output_path_def = f'{output_path}/{patient_name}/{date}__Studies/{name}'

    path_file_DWI = f'{path_file_RM}/{patient_name}/{date}__Studies/{name}'
    
    shutil.copytree(path_file_DWI, output_path_def)
    
#    except FileExistsError:
#        pass
#    
#        
        
        



#A = glob.glob(path_file_RM + '/*/*/*')

#'/media/leonardo/Dell_HD/RM_Patients_Anon/Patient02_AIM02/2011-06__Studies/Patient02_AIM02_MR_2011-06-29_100921_Rm.cranioencefalo.con.m.d.c-_dadc_n24__00000'
