#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:35:39 2019

@author: leonardo
"""

# script per unire le mask per i pazienti che ne hanno più di una

import numpy as np
import SimpleITK as sitk


Mask1_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient05/RT_nii/imp_mask_Brain2.nii'
Mask1_stk=sitk.ReadImage(Mask1_path)

Mask2_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient05/RT_nii/imp_mask_PTV asse.nii'
Mask2_stk=sitk.ReadImage(Mask2_path)

output_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient05/RT_nii/TOT.nii'

Mask1_np=sitk.GetArrayFromImage(Mask1_stk)
Mask2_np=sitk.GetArrayFromImage(Mask2_stk)

MaskTOT_np=Mask1_np+Mask2_np

MaskTOT_stk=sitk.GetImageFromArray(MaskTOT_np)

mask_spacing=Mask1_stk.GetSpacing()
mask_origin=Mask1_stk.GetOrigin()
mask_direction=Mask1_stk.GetDirection()


MaskTOT_stk.SetSpacing(mask_spacing)
MaskTOT_stk.SetOrigin(mask_origin)
MaskTOT_stk.SetDirection(mask_direction)

mask_TOT_spacing=MaskTOT_stk.GetSpacing()
mask_TOT_origin=MaskTOT_stk.GetOrigin()
mask_TOT_direction=MaskTOT_stk.GetDirection()



sitk.WriteImage(MaskTOT_stk, output_path, True)


