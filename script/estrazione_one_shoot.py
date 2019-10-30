#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:01:37 2019

@author: leonardo
"""


import sys 
sys.path.append('/home/leonardo/Scrivania/TESI/script/script_funzioni')

import estrattore_features_doseGy

image_path= '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient35/2015/Patient35_AIM35_RTDOSE_2015-08-10_112038_CSI_TomoTherapy.Planned.Dose_n1__00000/2.16.840.1.114362.1.11741058.22091046951.521052422.848.1262.dcm' 



mask_path= '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient35/RT_nii/TOT_PTV CSI.nii' 



output_path='/home/leonardo/Scrivania/TESI/features_estratte_bW1/Patient35.csv'

estrattore_features_doseGy.EstrattoreFeaturesDose(image_path,mask_path,output_path)