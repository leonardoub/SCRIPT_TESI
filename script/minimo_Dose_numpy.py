#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:35:45 2019

@author: leonardo
"""


import numpy as np
import SimpleITK as sitk

DOSE_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm' 
DOSEstk=sitk.ReadImage(DOSE_path)

Mask_path='/home/leonardo/Scrivania/paziente_prova/RTst_nii/mask_Body.nii'
Maskstk=sitk.ReadImage(Mask_path)


n=(DOSEnp>=99).sum()
m=(DOSEnp<99).sum()

nVoxelMask=(Masknp==1).sum()