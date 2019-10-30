#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:06:16 2019

@author: leonardo
"""


import sys 
sys.path.append('/home/leonardo/Scrivania/TESI/script/script_CT')

import estrattore_features_CT


import os
os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
patient_list=os.listdir()

for patient in patient_list:
          
    os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii')
    
       
    image_path=('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii/image.nii')
                 
                
    mask_list=os.listdir()
        
    for mask in mask_list:
        if 'MOD2' in mask:
            mask_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/' + mask 
                
    output_path='/home/leonardo/Scrivania/TESI/features/features_CT_estratte_bW1_MOD/' + patient + '.csv'
    
    estrattore_features_CT.EstrattoreFeaturesCT(image_path, mask_path,output_path, bW=1)


#si può forse ottimizzare facendolo girare da solo sui pazienti come è stato fatto con lo script per i plot, anche se ci possono essere problemi quando si blocca per problemi delle maschere
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    