# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#script che separa e salva i volumi contenenti le ADC dai volumi contenenti i gradienti nelle DWI



import pandas as pd
import nibabel as nib
import numpy as np
import glob
import os


path_main = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii'

path_folder_DWI_list = glob.glob(path_main + '/*/*')

path_DWI_list = glob.glob(path_main + '/*/*/*')

path_img_ADC_list = [i for i in path_DWI_list if '_ADC' in i]

path_img_list =[j.replace('_ADC','') for j in path_img_ADC_list]

for path_img, path_img_ADC in zip(path_img_list, path_img_ADC_list):
    
    img = nib.load(path_img)
    img_array = img.get_fdata()
    shape_img = img.shape
    
    img_ADC = nib.load(path_img_ADC)
    img_ADC_array = img_ADC.get_fdata()
    shape_img_ADC = img_ADC.shape
       
    l = shape_img[-1]

    ADC = img_ADC_array[:,:,:,l:]

    T=np.transpose(ADC, [3,0,1,2]) 
    
    for i, single_ADC in enumerate(T):
        
        out_fname = path_img.replace('-a', f'ADC_{i+1}')
        
        single_ADC=single_ADC.astype('float32')
        
        nib.Nifti1Image(single_ADC, img_ADC.affine).to_filename(out_fname)
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#    
#    
#
#    shape_ADC_1 = ADC_1.shape
#    
#    T=np.transpose(ADC_1, [3,0,1,2])
#    
#    
#    try:
#        
#        ADC_2 = img_ADC[:,:,:,l+1]
#        shape_ADC_2 = ADC_2.shape
#        
#    except IndexError:
#        pass
#    
#    
#



#img_ADC = nibabel.load(path_img_ADC).get_fdata()
#np.all(img == img_ADC[:,:,:,:7])