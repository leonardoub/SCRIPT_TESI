#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:12:23 2019

@author: leonardo
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

A=['01','02','03','04','05','06','08','09','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']

#L=['01','02']

for i in A:
    os.chdir('/home/leonardo/Scrivania/Patients/'+i+'/features_estratte')
    mask_features_list=os.listdir()

    listaMedie=[]
    listaStdv=[]
    
    mask_features_list2=[]
    #mi serve soltanto per mettere i nomi delle ROI sull'asse delle ascisse
    
    for mask_features in mask_features_list:
    
            mask_features_path='/home/leonardo/Scrivania/Patients/'+i+'/features_estratte/'+ mask_features    
     
            df=pd.read_csv(mask_features_path)
            
            name_list=list(df.iloc[:,1])
    
            ind1=name_list.index('original_firstorder_Mean')
            ind2=name_list.index('original_firstorder_Variance')
   
            
            
            Media=float(df.iloc[ind1,2])
            Varianza=float(df.iloc[ind2,2])
            Stdv=np.sqrt(Varianza)
            
            listaMedie.append(Media)
            
            listaStdv.append(Stdv)
            
            mask_name1=mask_features.replace('.nii.csv','')
            mask_name2=mask_name1.replace('_',' ')
            mask_name3=mask_name2.replace('mask','')
            mask_features_list2.append(mask_name3)
            #mi serve soltanto per mettere i nomi delle ROI sull'asse delle ascisse
            
            #ora devo fare i plot e salvarli, ogni istogramma che contiene la dose media in ogni roi va salvato nella cartella del paziemte
            
    N=len(mask_features_list)
            
    indici=np.arange(N)
            
    width=0.5
            
    p1=plt.bar(indici, listaMedie, width, color=(0.2, 0.4, 0.6, 0.6), yerr=listaStdv)
            
    plt.ylabel('Dose media')
    plt.title('Dose media e standard deviation nelle ROI')
    plt.xticks(indici, mask_features_list2, rotation='vertical')
    plt.yticks(np.arange(0,81,5))
    
    plt.savefig('/home/leonardo/Scrivania/Patients/'+i+'/plot/plot_paziente_no_image_'+i+'.pdf',  bbox_inches = "tight")
    plt.close()    
        
            
            
            
            
            

#plt.close() è importante perche sennò mi disegna tutti i grafici sovrapposti
#c=df.iloc[43,1]
    
#bbox_inches = "tight" fa entrare anche i nomi sotto all'asse delle ascisse nell'immagine, senza venivano tagliati
    
    
    