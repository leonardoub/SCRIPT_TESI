#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:06:16 2019

@author: leonardo
"""


import sys 
sys.path.append('/home/leonardo/Scrivania/TESI/script/script_funzioni')

import estrattore_features_doseGy 


import os
os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
patient_list=os.listdir()

for patient in patient_list:
          
    os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient)
    dir_list=os.listdir()
       
    if len(dir_list)==4:
               
        for i in dir_list:
            if 'RTDOSE' in i:
                os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/'+i)
                file_list=os.listdir()
                for file in file_list:
                    if '.dcm' in file:
                        image_path=('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/'+i+'/'+file)
                
        os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/'+patient+'/RT_nii')
        mask_list=os.listdir()
            
        for mask in mask_list:
            if 'TOT' in mask:
                mask_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/' + mask 
                
        output_path='/home/leonardo/Scrivania/TESI/features_estratte_bW1/' + patient + '.csv'
    
        estrattore_features_doseGy.EstrattoreFeaturesDose(image_path,mask_path,output_path)


#si può forse ottimizzare facendolo girare da solo sui pazienti come è stato fatto con lo script per i plot, anche se ci possono essere problemi quando si blocca per problemi delle maschere
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    