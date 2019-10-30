#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:08:30 2019

@author: leonardo
"""


from dcmrtstruct2nii import dcmrtstruct2nii

import os
os.chdir('/home/leonardo/Scrivania/Patients Anonymized')
patients_list=os.listdir()

for patient in patients_list:
    os.chdir('/home/leonardo/Scrivania/Patients Anonymized/'+patient)
    folder_list=os.listdir()
    
    for folder in folder_list:
        if 'RTst' in folder:
           os.chdir('/home/leonardo/Scrivania/Patients Anonymized/'+patient+'/'+folder)
           st_list=os.listdir()
           for st in st_list:
               if 'dcm' in st:
                   RT_path='/home/leonardo/Scrivania/Patients Anonymized/'+patient+'/'+folder+'/'+st
       
        elif 'CT' in folder:
            CT_path='/home/leonardo/Scrivania/Patients Anonymized/'+patient+'/'+folder
        
#        continue
            
    output_path='/home/leonardo/Scrivania/Patients Anonymized/'+patient+'/RT_nii/'
        
    dcmrtstruct2nii(RT_path,CT_path,output_path,structures=None,gzip=False,mask_background_value=0,mask_foreground_value=1,convert_original_dicom=True)
                            
                       
            
            
    