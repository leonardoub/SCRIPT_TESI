#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:39:28 2019

@author: leonardo
"""


import numpy as np
import SimpleITK as sitk
import os


os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
patient_list=os.listdir()

for patient in patient_list:

    CT_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/image.nii'
    CTstk=sitk.ReadImage(CT_path)
    
    os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii')
    mask_list=os.listdir()
    
    for mask in mask_list:
        if 'TOT' in mask:
            Mask_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/' + mask
    
    Maskstk=sitk.ReadImage(Mask_path)
    
    output_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/MOD2.nii'
    
    CTnp=sitk.GetArrayFromImage(CTstk)
    Masknp=sitk.GetArrayFromImage(Maskstk)
    
#    CTnp[CTnp==0]=1
#    A=CTnp*Masknp
#    A[A>65]=0
#    A[A!=0]=1

    Masknp[CTnp>=200]=0    
    Masknp[CTnp<-100]=0
    
    Maskstk1=sitk.GetImageFromArray(Masknp)
    
    Mask_spacing=Maskstk.GetSpacing()
    Mask_origin=Maskstk.GetOrigin()
    Mask_direction=Maskstk.GetDirection()
        
        
    Maskstk1.SetSpacing(Mask_spacing)
    Maskstk1.SetOrigin(Mask_origin)
    Maskstk1.SetDirection(Mask_direction)
    
    sitk.WriteImage(Maskstk1, output_path, True)



#vengono prese porzioni di vuoto, non va bene 





#
#
#CT_size=CTstk.GetSize()
#CT_spacing=CTstk.GetSpacing()
#CT_depth=CTstk.GetDepth()
#CT_dimension=CTstk.GetDimension()
#CT_direction=CTstk.GetDirection()
#CT_numberofpixels=CTstk.GetNumberOfPixels()
#CT_origin=CTstk.GetOrigin()
#
#
#
#MASK_size=Maskstk.GetSize()
#MASK_spacing=Maskstk.GetSpacing()
#MASK_depth=Maskstk.GetDepth()
#MASK_dimension=Maskstk.GetDimension()
#MASK_direction=Maskstk.GetDirection()
#MASK_numberofpixels=Maskstk.GetNumberOfPixels()
#MASK_origin=Maskstk.GetOrigin()
#
#
#Maskstk.SetDirection(CT_direction)
#Maskstk.SetOrigin(CT_origin)
#
#Masknp1=Masknp=sitk.GetArrayFromImage(Maskstk)
#
#
#A1=CTnp*Masknp1
#FACENDO SET ORIGIN E DIRECTION NON CAMBIA NULLA


















