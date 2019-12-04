#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:41:36 2019

@author: leonardo
"""

import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt


#ADC_path = '/home/leonardo/Scrivania/data/Patient23/Patient23_AIM23_MR_2014-06-05_144559_RM.ENCEFALO_DWI.HR.SENSE_n306__00000/ADC_1.nii'
#MASK_BRAIN_path = '/home/leonardo/Scrivania/data/Patient23/transformed_using_MASK_BRAIN_HANDMADE.nii'

ADC_path = '/home/leonardo/Scrivania/data/Patient25/Patient25_AIM25_MR_2014-07-31_083951_RM.ENCEFALO.e.midollo.SENZA.E.CON.MDC_DWI.HR.SENSE_n288__00000/ADC_1.nii'
MASK_BRAIN_path = '/home/leonardo/Scrivania/data/Patient25/transformed_using_MASK_BRAIN_HANDMADE.nii'

ADC_sitk = sitk.ReadImage(ADC_path)
MASK_sitk = sitk.ReadImage(MASK_BRAIN_path)

ADC_np = sitk.GetArrayFromImage(ADC_sitk)
MASK_np = sitk.GetArrayFromImage(MASK_sitk)

A = ADC_np*MASK_np
B=A.flatten()

B.sort()

C=A[A>0]
C.sort()

plt.hist(B, 100, range=(0, 900))

