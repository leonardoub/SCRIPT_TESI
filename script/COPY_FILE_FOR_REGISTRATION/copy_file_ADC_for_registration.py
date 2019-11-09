#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:45:58 2019

@author: leonardo
"""

#preparare file per la registrazione, creare una cartella con ADC_1.nii ADC_2.nii 
import os
import glob
from shutil import copyfile


path_output_ADC = '/home/leonardo/Scrivania/CT_DWI_registration/ADC'  
path_DWI_input = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii'

patient_list = os.listdir(path_DWI_input) 
patient_list = [i[:9] for i in patient_list]

path_DWI_list = glob.glob(path_DWI_input + '/*/*/*')

path_img_ADC_list = [i for i in path_DWI_list if 'ADC_' in i]

#for patient in patient_list:
#    os.makedirs(f'{path_output_DWI}/{patient}')
  
for patient in patient_list:

    dst = f'{path_output_ADC}/{patient}'

    for src in path_img_ADC_list:
        
        a = src.rsplit('/')[-2]
        b = src.rsplit('/')[-1]
        
        dst_def = f'{dst}/{a}/{b}' 
        
        if patient in src:
                
                os.makedirs(f'{dst}/{a}', exist_ok=True)
                
                copyfile(src, dst_def)
                
        else:
            pass 
            
            




#copyfile(src, dst)