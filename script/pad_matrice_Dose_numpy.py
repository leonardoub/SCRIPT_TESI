#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:17:09 2019

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

DOSEnp1=np.flip(DOSEnp,0)


#indexmax=np.where(DOSEnp1==31950)

DOSEnp2=np.pad(DOSEnp1,((0,0),(23,25),(0,0)),'constant')


DOSEnp3=DOSEnp2*Masknp

#Media=DOSEnp3.mean()
#non posso calcolare la media così perchè divido per tutti il numero di voxel totali e non solo quelli della mask

#Min=DOSEnp3.min()
#non posso calcolare il min così perchè viene banalmente zero lo devo calcolare solo sui voxel della mask


#STDV=DOSEnp3.std()
#non posso calcolare la stdv così perchè così considero tutti i voxel e non solo quelli della mask

N=(DOSEnp3!=0).sum()
Media=DOSEnp3.sum()/N



S=np.sort(DOSEnp3, axis=None)
T=S[S.nonzero()]
Min=T[0]

Max=np.max(DOSEnp3)

Media2=np.mean(T)

stdv=np.std(T)





