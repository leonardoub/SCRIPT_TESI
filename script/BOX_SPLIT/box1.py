#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:03:15 2019

@author: leonardo
"""

import numpy as np
import SimpleITK as sitk

Mask_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient01/RT_nii/TOT.nii'
Maskstk=sitk.ReadImage(Mask_path)
Masknp=sitk.GetArrayFromImage(Maskstk)
Masknp=Masknp.transpose(2,1,0)

tmp = Masknp 
stepSize = 50
w_width, w_height, w_thickness = 50, 50 # window size
for x in range(0, Masknp.shape[0], int(stepSize/2)):
   for y in range(0, Masknp.shape[1], int(stepSize/2)):
       for z in range(0, Masknp.shape[2], int(stepSize/2)):
       window = Masknp[x:x + w_width, y:y + w_height, z: z + w_thickness]
       