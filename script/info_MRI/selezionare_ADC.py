# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#voglio separare i volumi delle ADC dai volumi dei gradienti

import pandas as pd
import nibabel as nb
import numpy as np
import glob
import os

path_main = '/home/leonardo/Scrivania/TESI/MRI_DWI_nii'

path_folder_DWI_list = glob.glob(path_main + '/*/*')

path_DWI_list = glob.glob(path_main + '/*/*/*')

path_img_ADC_list = [i for i in path_DWI_list if '_ADC' in i]

path_img_list =[j.replace('_ADC','') for j in path_img_ADC_list]


img_ADC = nb.load(A).get_fdata()
shape_img_ADC = img_ADC.shape

img = nb.load(B).get_fdata()
shape_img = img.shape

l = shape_img[-1]

ADC_1 = img_ADC[:,:,:,l]
shape_ADC_1 = ADC_1.shape

T=np.transpose(ADC_1, [3,0,1,2])


try:
    
    ADC_2 = img_ADC[:,:,:,l+1]
    shape_ADC_2 = ADC_2.shape
    
except IndexError:
    pass






#img_ADC = nibabel.load(path_img_ADC).get_fdata()
#np.all(img == img_ADC[:,:,:,:7])