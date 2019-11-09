#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:18:00 2019

@author: leonardo
"""

#script per moltiplicare CT e MASK
#per creare la cartella di tipo_2


import numpy as np
import SimpleITK as sitk
import glob
import os


input_path = '/home/leonardo/Scrivania/file_for_registration/CT_and_MASK'

#path_file_list = glob.glob(input_path + '/*/*')
#path_CT_list = [i for i in path_file_list if 'CT' in i]
#path_MASK_list = [j for j in path_file_list if 'MASK' in j]

patient_list = os.listdir(input_path) 

for patient in patient_list:
    CT_path = f'{input_path}/{patient}/CT.nii'
    MASK_path = f'{input_path}/{patient}/MASK_TOT.nii'
    
    
    CT_stk=sitk.ReadImage(CT_path)
    MASK_stk=sitk.ReadImage(MASK_path)
    
    CT_np=sitk.GetArrayFromImage(CT_stk)
    MASK_np=sitk.GetArrayFromImage(MASK_stk)
    
    CTxMASK_np = CT_np*MASK_np
    
    CTxMASK_stk = sitk.GetImageFromArray(CTxMASK_np)
    
    #BISOGNA RISOLVERE IL PROBLEMA DEL VOXEL SPACING
    
    MASK_spacing=MASK_stk.GetSpacing()
    MASK_origin=MASK_stk.GetOrigin()
    MASK_direction=MASK_stk.GetDirection()
        
        
    CTxMASK_stk.SetSpacing(MASK_spacing)
    CTxMASK_stk.SetOrigin(MASK_origin)
    CTxMASK_stk.SetDirection(MASK_direction)
    
    sitk.WriteImage(CTxMASK_stk, f'{input_path}/{patient}/CTxMASK_TOT.nii', True)










#PROVA    
#    
#    
#path_CT = path_CT_list[0] 
#
#path_MASK = path_MASK_list[0]
#
#CT_stk = sitk.ReadImage(path_CT)
#MASK_stk = sitk.ReadImage(path_MASK)    
# 
#CT_np=sitk.GetArrayFromImage(CT_stk)
#MASK_np=sitk.GetArrayFromImage(MASK_stk)
#
#A_np = CT_np*MASK_np
#
#A = sitk.GetImageFromArray(A_np)
#
#
#MASK_spacing=MASK_stk.GetSpacing()
#MASK_origin=MASK_stk.GetOrigin()
#MASK_direction=MASK_stk.GetDirection()
#    
#    
#A.SetSpacing(MASK_spacing)
#A.SetOrigin(MASK_origin)
#A.SetDirection(MASK_direction)
#     
#sitk.WriteImage(A, '/home/leonardo/Scrivania/B2.nii', True)
#
#


#NON FUNZIONA
#    
#path_CT = path_CT_list[0] 
#
#path_MASK = path_MASK_list[0]
#
#CT_stk = sitk.ReadImage(path_CT)
#MASK_stk = sitk.ReadImage(path_MASK, sitk.sitkFloat32)
#
#A = CT_stk*MASK_stk
#
#     
#sitk.WriteImage(A, '/home/leonardo/Scrivania', True)
#



















