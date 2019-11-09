#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:25:21 2019

@author: leonardo
"""

#preparare file per la registrazione, creare una cartella con CT.nii e MASK.nii
#per creare cartella di tipo _2

import os
import glob
from shutil import copyfile

path_output_CT_MASK = '/home/leonardo/Scrivania/CT_ADC_DOSE_MASK_registration_2' 
path_DWI_input = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii'  #serve solo per creare la lista di pazienti da selezionare

patient_list = os.listdir(path_DWI_input) 
patient_list = [i[:9] for i in patient_list]

#for patient in patient_list:
#    os.makedirs(f'{path_output_CT}/{patient}')


for patient in patient_list:
    
     dst_CT = f'{path_output_CT_MASK}/{patient}/CT.nii'
     
     path_input_CT = f'/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/{patient}/RT_nii/image.nii'

     copyfile(path_input_CT, dst_CT)
     
     
     dst_MASK = f'{path_output_CT_MASK}/{patient}/MASK_TOT.nii'
     
     MASK_list = os.listdir(f'/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/{patient}/RT_nii')
     
     MASK_list_TOT = [i for i in MASK_list if 'TOT' in i]
     
     MASK = MASK_list_TOT[0]
     
     path_input_MASK = f'/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/{patient}/RT_nii/{MASK}'
     
     copyfile(path_input_MASK, dst_MASK)

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     