#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:58:43 2019

@author: leonardo
"""

import numpy as np
import SimpleITK as sitk
import argparse
import matplotlib.pyplot as plt
import scipy.stats 


stp=50


Mask_path='/home/leonardo/Scrivania/data_registered/Patient56/MASK_TOT.nii'


Maskstk = sitk.ReadImage(Mask_path)
Masknp = sitk.GetArrayFromImage(Maskstk)

num_slices = Masknp.shape[0]

A = Masknp.sum(axis=(1,2)) #non c'è bisogno di un ciclo for sulle slices, lo fa da solo

mask = [np.all(A[i-stp:i]==sorted(A[i-stp:i]) and A[i]!=0) for i in range(num_slices)]

B = A[::-1]

p = np.percentile(A, 87)

#indices = np.where(A >= 450)
#index = indices[0][0]
#Masknp[:index,:,:] = 0
#
#plt.plot(A,'r+')
#




scipy.io()
loadmat