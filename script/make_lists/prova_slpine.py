#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:58:43 2019

@author: leonardo
"""

import numpy as np
import SimpleITK as sitk
import argparse


Mask_path='/home/leonardo/Scrivania/data_registered/data/Patient48/MASK_TOT.nii'


Maskstk = sitk.ReadImage(Mask_path)
Masknp = sitk.GetArrayFromImage(Maskstk)

num_slices = Masknp.shape[0]

A = Masknp.sum(axis=(1,2)) #non c'è bisogno di un ciclo for sulle slices, lo fa da solo

#indices = np.where(A >= 450)
#index = indices[0][0]
#Masknp[:index,:,:] = 0



