#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:29:13 2019

@author: leonardo
"""

import numpy as np
import SimpleITK as sitk

DOSE_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm' 
DOSEstk=sitk.ReadImage(DOSE_path)

Mask_path='/home/leonardo/Scrivania/paziente_prova/RTst_nii/mask_Body.nii'
Maskstk=sitk.ReadImage(Mask_path)

DOSEnp=sitk.GetArrayFromImage(DOSEstk)
Masknp=sitk.GetArrayFromImage(Maskstk)

#A=DOSEnp*Masknp

Max=np.max(DOSEnp)

indici=np.where(DOSEnp==31950)

Mean=np.mean(DOSEnp)

DOSEnp1=DOSEnp

DOSEnp1[DOSEnp1<Mean]=0

Max1=np.max(DOSEnp1)

ones=(Masknp==1).sum()
#zeros=(Masknp==0).sum()

n=(DOSEnp1>0).sum()
#m=(DOSEnp1==0).sum()

Mean1=DOSEnp1.sum()/ones

Mean2=DOSEnp1.sum()/n

#confrontare mean1 con la media ottenuta con Pyradiomics+correctMask --> NON TORNA 
#Mean2 è anche peggio





