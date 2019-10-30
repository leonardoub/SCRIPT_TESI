#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:08:30 2019

@author: leonardo
"""


import dicom2nifti


import os
os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
patients_list=os.listdir()

for patient in patients_list:
    os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient)
    folder_list=os.listdir()
    
    for folder in folder_list:
        if 'kVCT' in folder:
            CT_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/'+folder
        continue
            
    output_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/CT.nii'
        
    dicom2nifti.dicom_series_to_nifti(CT_path,output_path)
                            
                       
            
            
    