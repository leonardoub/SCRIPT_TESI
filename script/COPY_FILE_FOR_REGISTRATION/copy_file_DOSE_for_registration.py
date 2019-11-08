#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:50:48 2019

@author: leonardo
"""

#preparare file per la registrazione, creare una cartella con la distribuzione di dose

import os
import glob
from shutil import copyfile


path_output_DOSE = '/home/leonardo/Scrivania/CT_DWI_registration/DOSE'  
path_DWI_input = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii'  #serve solo per creare la lista di pazienti da selezionare

patient_list = os.listdir(path_DWI_input) 
patient_list = [i[:9] for i in patient_list]

#for patient in patient_list:
#    os.makedirs(f'{path_output_DOSE}/{patient}')

for patient in patient_list:
    
    dst_DOSE = f'{path_output_DOSE}/{patient}/DOSE_DISTR.dcm'
    
    path_input_folder = f'/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/{patient}'

    path_input_folder_list = glob.glob(path_input_folder + '/*')
    
    path_input_DOSE = [i for i in path_input_folder_list if 'RTDOSE' in i][0]
    
    DOSE_list = os.listdir(path_input_DOSE)
    
    DOSE_list_dcm = [j for j in DOSE_list if '.dcm' in j]
    
    DOSE = DOSE_list_dcm[0]
    
    path_input_DOSE = f'{path_input_DOSE}/{DOSE}'
  
    copyfile(path_input_DOSE, dst_DOSE)
    
    
    
    
    
    