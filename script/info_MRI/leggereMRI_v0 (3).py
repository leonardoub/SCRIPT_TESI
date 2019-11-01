#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:00:28 2019

@author: lpalumbo
"""

" This function extract header information from MRI files and create a table with information of interest "

import os
import pandas as pd
import glob 
import logging
import numpy as np
import pydicom
from datetime import datetime
from datetime import timedelta

import SimpleITK as stk

logging.basicConfig(level=logging.INFO)
path_file_RM='/Volumes/Dell_HD/RM_Patients_Anon'
path_info_table='/Users/lpalumbo/Desktop/AIM_mancano_imm_da_copiare/Tesi_Leonardo_progetto_AIM/Database/AIM_FI/Elenco_Pz_AIM_ok_Pisa_2.xlsx'

def read_RMfile(path_file_RM,path_info_table):
    
    ''' Questa funzione riceve in input il percorso della cartella in cui si trovano le risonanze, 
    ed il percorso in cui si trova la tabella di Piffer completa. Deve restituire un file excel 
     in cui è presente per ciascun paziente l'informazione delle sequenze di risonanza acquisite almeno 6 mesi dopo il piano di trattamento'''

    Table_dati=pd.read_excel(path_info_table)
    df0=list(Table_dati['Anonymized Nome - ID'])
    #print(df0)
    df1= list(Table_dati['RADIO DATE'])
    #chiavi=[df0[k] for k, index in enumerate(df0)]   #[:-6]
    #print(chiavi)
    diz_data_trattamento={c:v for (c,v) in zip(df0,df1)}
    #print(diz_data_trattamento)
    df = pd.DataFrame({'Patient_ID': [],'Percorso_RM':[],'Protocol_name/Pixel_Spacing/Space_Between_slices':[],'Righe-Colonne':[],'NumSlice':[]})

    delta=timedelta(days=150)
    lista_date=[]
    data_acquisizione=[]
    protocol_name=[]
    pixel_spacing=[]
    slice_betweenslices=[]
    diz_path={}
    D={}
    
    for name in glob.glob(path_file_RM+'/*'):
        #print(name)
        file=os.listdir(name) 
        lista_date=[]
        for f in file:
            #print(f)
            datatime_object=datetime.strptime(f[:-9],'%Y-%m')
            #print(datatime_object)
            lista_date.append(datatime_object)
            #print(lista_date)
            array_date=np.array([lista_date])
            diz_path[name[-15:]]=lista_date   # [-15:-6]]
            #print(diz_path)
    
    for key in diz_data_trattamento.keys():
    
        try:
        
            data_RM=np.array(diz_path[key])
            diz_path[key]=np.array(diz_path[key])[data_RM > diz_data_trattamento[key]+delta]  # > | < 
            diz_path[key].sort()
            D[key]=diz_path[key][1] # scegli l'indice giusto ( dipende dalla cartella) # 0 | 1 | -1
            percorso_RM=path_file_RM+'/'+key+'/'+datetime.strftime(D[key],'%Y-%m')
            percorso_RM=percorso_RM+'__Studies'
            file_RM=os.listdir(percorso_RM)
            print(D)
               
        except KeyError:
        
            diz_path[key]='non presente'
            D[key]='non presente'
    
        except IndexError:
            diz_path[key]='nessuna Risonanza post trattamento'
            D[key]='nessuna Risonanza post trattamento (6 mesi)'
            
    
    
        for seq in file_RM:
            #print(seq)
            var_mr='_MR_'
            
            if ('_MR_' in seq or '_mr_' in seq):
  
                file_dcm=os.listdir(percorso_RM+'/'+seq)
        
                #print(seq)
    
                RefDs_RT=pydicom.read_file(percorso_RM+'/'+seq+'/'+file_dcm[0])
               
                try: 
            
                    data_acquisizione=(RefDs_RT.AcquisitionDate)
                    protocol_name=RefDs_RT.ProtocolName
                    pixel_spacing=[RefDs_RT.PixelSpacing, RefDs_RT.SpacingBetweenSlices]
                    slice_betweenslices=RefDs_RT.SliceThickness
                    matrix=[RefDs_RT.Rows,RefDs_RT.Columns]
                    slice_number=len(file_dcm)-1
                    df =df.append({'Patient_ID':key, 'Percorso_RM': seq, 'Protocol_name/Pixel_Spacing/Space_Between_slices':[protocol_name,pixel_spacing,slice_betweenslices],'Righe-Colonne': matrix,'NumSlice':slice_number}, ignore_index=True)

                except AttributeError:
                
                    data_acquisizione='empty field'
                    protocol_name='empty field'
                    pixel_spacing='empty field'
                    slice_betweenslices='empty field'
                    matrix='empty field'
                    df =df.append({'Patient_ID':key, 'Percorso_RM': seq, 'Protocol_name/Pixel_Spacing/Space_Between_slices':[protocol_name,pixel_spacing,slice_betweenslices],'Righe-Colonne': matrix,'NumSlice':slice_number}, ignore_index=True)

            else:
                pass

    export_excel = df.to_excel (r'/Users/lpalumbo/Desktop/export_info_RM_funzione_successiva_a_6mesi.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path
    return df