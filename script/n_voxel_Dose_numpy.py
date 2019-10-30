#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:20:20 2019

@author: leonardo
"""

#voglio confrontare (usando numpy): 
#il numero di voxel della dose che entra in un range di +-stdv dalla media (media e stdv calcolare con pyradiomics+correctMask usando la maschera Body) 
#col numero di voxel della maschera con valore==1



import numpy as np
import SimpleITK as sitk

DOSE_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm' 
DOSEstk=sitk.ReadImage(DOSE_path)

Mask_path='/home/leonardo/Scrivania/paziente_prova/RTst_nii/mask_Body.nii'
Maskstk=sitk.ReadImage(Mask_path)


DOSEnp=sitk.GetArrayFromImage(DOSEstk)
Masknp=sitk.GetArrayFromImage(Maskstk)

media=11087.162509863952

varianza=100609209.1435371

stdv=np.sqrt(varianza)

A=media-stdv

B=media+stdv

N=((DOSEnp>=A) & (DOSEnp<=B)).sum()

M=(Masknp==1).sum()


N1=(DOSEnp>=A).sum()


#NON POSSO USARE 3 STDV PERCHÈ LA STDV È MOLTO ALTA, LA MEDIA E LA DEVIAZIONE STANDARD DIFFERISCONO DI POCO




