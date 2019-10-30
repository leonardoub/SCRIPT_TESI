#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:35:39 2019

@author: leonardo
"""

# script per unire le mask per i pazienti che ne hanno più di una

import numpy as np
import SimpleITK as sitk
import os


os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
patient_list=os.listdir()

for patient in patient_list:
    
    os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii')
    mask_list=os.listdir()
    
    imp_list=[]
    for i in mask_list:
        if 'imp' in i:
            imp_list.append(i)
   
    if len(imp_list)==2:
         
        Mask1_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii/'+imp_list[0]
        Mask1_stk=sitk.ReadImage(Mask1_path)
        
        Mask2_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii/'+imp_list[1]
        Mask2_stk=sitk.ReadImage(Mask2_path)
        
        output_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii/TOT.nii'
        
        Mask1_np=sitk.GetArrayFromImage(Mask1_stk)
        Mask2_np=sitk.GetArrayFromImage(Mask2_stk)
        
        MaskTOT_np=Mask1_np+Mask2_np
        
        MaskTOT_stk=sitk.GetImageFromArray(MaskTOT_np)
        
        Mask1_spacing=Mask1_stk.GetSpacing()
        Mask1_origin=Mask1_stk.GetOrigin()
        Mask1_direction=Mask1_stk.GetDirection()
        
        
        MaskTOT_stk.SetSpacing(Mask1_spacing)
        MaskTOT_stk.SetOrigin(Mask1_origin)
        MaskTOT_stk.SetDirection(Mask1_direction)
        
        
        sitk.WriteImage(MaskTOT_stk, output_path, True)


