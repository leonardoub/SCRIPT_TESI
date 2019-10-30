#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:07:52 2019

@author: leonardo
"""

import sys 
sys.path.append('/home/leonardo/Scrivania/paziente_prova/script/provo a fare gli script di Letizia funzioni')

import estrattore_features_doseGy 

image_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm'
mask_path='/home/leonardo/Scrivania/paziente_prova/RT_4_nii/mask_ctv midollo.nii' 
output_path='/home/leonardo/Scrivania/paziente_prova/DOSE_features_midollo_Gy.csv'

estrattore_features_doseGy.EstrattoreFeaturesDose(image_path,mask_path,output_path)


