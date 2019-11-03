#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:38:39 2019

@author: leonardo
"""



import os
import pandas as pd
import glob 
import logging
import numpy as np
import pydicom
from datetime import datetime
from datetime import timedelta
import SimpleITK as stk
import ezodf
from pandas_ods_reader import read_ods

logging.basicConfig(level=logging.INFO)
path_file_RM = '/media/leonardo/Dell_HD/RM_Patients_Anon'
path_info_table = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Elenco_Pz_AIM_ok_Pisa_clean.ods' 

Table_dati = read_ods(path_info_table, 1)

df0 = list(Table_dati['Anonymized Nome - ID'])
df1 = list(Table_dati['RADIO DATE'])

df1 = [datetime.strptime(i, '%Y-%m-%d') for i in df1]

dict_data_trattamento = {c:v for (c, v) in zip(df0, df1)}

df = pd.DataFrame({'Patient_ID': [], 'Percorso_RM': [], 'Protocol_name/Pixel_Spacing/Space_Between_slices': [],
                   'Righe-Colonne': [], 'NumSlice': []})

delta = timedelta(days = 150)
lista_date_RM = []
data_acquisizione = []
protocol_name = []
pixel_spacing = []
slice_betweenslices = []
dict_date_RM = {}
D = {}


for name in glob.glob(path_file_RM + '/*'):
    file = os.listdir(name)
    lista_date_RM = []
    for f in file:
        datatime_object = datetime.strptime(f[:-9], '%Y-%m')
        lista_date_RM.append(datatime_object)
        dict_date_RM[name[-15:]] = lista_date_RM


#da questo ciclo esce un dizionario avente per chiavi i PT e 
#per valore una lista contenente tutte le date relative alle MR
                
for key in dict_data_trattamento.keys():
        
    try:
        array_date_RM = np.array(dict_date_RM[key])
        dict_date_RM[key] = array_date_RM [array_date_RM < dict_data_trattamento[key]]
        dict_date_RM[key].sort()
        D[key] = dict_date_RM[key][-1]
        path_RM = path_file_RM + '/' + key + '/' + datetime.strftime(D[key], '%Y-%m') 
        path_RM = path_RM + '__Studies/'
        file_RM_selected = os.listdir(path_RM)
            
    except KeyError:
        
        dict_date_RM[key] = 'Non presente'
        D[key] = 'Non presente'
               
    except IndexError:
            
        dict_date_RM[key] = 'nessuna Risonanza'
        D[key] = []
        path_RM = ''
        file_RM_selected = []
        
    if file_RM_selected != []:
        
        for sequence in file_RM_selected:
            
            if (('_MR_' in sequence or '_mr_' in sequence)  and ('3D' in sequence)):
                
                file_RM_dcm = os.listdir(path_RM + sequence)
                
                RefDs_RM = pydicom.read_file(path_RM + '/' + sequence + '/' + file_RM_dcm[0])
                
                try: 
            
                    data_acquisizione = (RefDs_RM.AcquisitionDate)
                    protocol_name = RefDs_RM.ProtocolName
                    pixel_spacing = [RefDs_RM.PixelSpacing, RefDs_RM.SpacingBetweenSlices]
                    slice_betweenslices = RefDs_RM.SliceThickness
                    matrix = [RefDs_RM.Rows,RefDs_RM.Columns]
                    slice_number = len(file_RM_dcm)-1
                    df = df.append({'Patient_ID': key, 'Percorso_RM': sequence,
                                   'Protocol_name/Pixel_Spacing/Space_Between_slices': [protocol_name, pixel_spacing, slice_betweenslices],
                                   'Righe-Colonne': matrix, 'NumSlice': slice_number}, ignore_index = True)

                except AttributeError:
                
                    data_acquisizione = 'empty field'
                    protocol_name = 'empty field'
                    pixel_spacing = 'empty field'
                    slice_betweenslices = 'empty field'
                    matrix = 'empty field'
                    df = df.append({'Patient_ID': key, 'Percorso_RM': sequence, 
                                    'Protocol_name/Pixel_Spacing/Space_Between_slices': [protocol_name, pixel_spacing, slice_betweenslices],
                                    'Righe-Colonne': matrix, 'NumSlice': slice_number}, ignore_index = True)

            else:
                pass

    else:
        pass

export_excel = df.to_excel ('/home/leonardo/Scrivania/TESI/tabelle_MRI/estratte_da_me/3D/export_info_RM_3D_pre.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

         
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    







