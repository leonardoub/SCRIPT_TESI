#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:35:55 2019

@author: lpalumbo
"""

# Prove con libreria Pyradiomics 

import pandas as pd

import radiomics 
import SimpleITK as sitk
import numpy as np
import sys, os

CT_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/CT_2011-09-29_075800_TomoTherapy.Patient.Disease_kVCT.Image.Set_n232__00000'
ROI_path='/home/leonardo/Scrivania/paziente_prova/RT_nii'



# Read Image CT (.dcm)
reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(CT_path)
reader.SetFileNames(dicom_names)
CT_sitk = reader.Execute()

# Info header CT

CT_size=CT_sitk.GetSize()
CT_spacing=CT_sitk.GetSpacing()
CT_depth=CT_sitk.GetDepth()
CT_dimension=CT_sitk.GetDimension()
CT_direction=CT_sitk.GetDirection()
CT_numberofpixels=CT_sitk.GetNumberOfPixels()
CT_origin=CT_sitk.GetOrigin()


# Read ROI (.nii)
ROI_sitk=sitk.ReadImage(ROI_path+'/mask_ptv encefalo.nii')


# Info header ROI

ROI_size=ROI_sitk.GetSize()
ROI_spacing=ROI_sitk.GetSpacing()
ROI_depth=ROI_sitk.GetDepth()
ROI_dimension=ROI_sitk.GetDimension()
ROI_direction=ROI_sitk.GetDirection()
ROI_numberofpixels=ROI_sitk.GetNumberOfPixels()
ROI_origin=ROI_sitk.GetOrigin()

ROI_np=sitk.GetArrayFromImage(ROI_sitk)
#ROI_np=ROI_np.transpose(2,1,0)

ROI_np[ROI_np==255]=1

#ROI_np=ROI_np.transpose(2,1,0)

ROI_sitk_1=sitk.GetImageFromArray(ROI_np) #N.B GetImageFromArray cambia lo spacing e l'origine :(

ROI_sitk_1.SetOrigin(ROI_origin)
ROI_sitk_1.SetSpacing(ROI_spacing)

ROI_size1=ROI_sitk_1.GetSize()
ROI_spacing1=ROI_sitk_1.GetSpacing()
ROI_depth1=ROI_sitk_1.GetDepth()
ROI_dimension1=ROI_sitk_1.GetDimension()
ROI_direction1=ROI_sitk_1.GetDirection()
ROI_numberofpixels1=ROI_sitk_1.GetNumberOfPixels()
ROI_origin1=ROI_sitk_1.GetOrigin()


from radiomics import imageoperations


ROI_sitk_2=imageoperations.getMask(ROI_sitk_1, label=1)

ROI_size2=ROI_sitk_2.GetSize()
ROI_spacing2=ROI_sitk_2.GetSpacing()
ROI_depth2=ROI_sitk_2.GetDepth()
ROI_dimension2=ROI_sitk_2.GetDimension()
ROI_direction2=ROI_sitk_2.GetDirection()
ROI_numberofpixels2=ROI_sitk_2.GetNumberOfPixels()
ROI_origin2=ROI_sitk_2.GetOrigin()

#Estrarre le features using pyradiomics 

from radiomics import featureextractor 

params = os.path.join('/home/leonardo/pyradiomics', "examples", "exampleSettings", "Params.yaml")

extractor = featureextractor.RadiomicsFeatureExtractor(params)
result = extractor.execute(CT_sitk,ROI_sitk_2) # type(result), particolare sottoclasse del dizionario che mantiene 
# l'ordine con cui i vari elementi sono stati aggiunti

features=dict()

import pandas as pd
for key,value in result.items():
    print(key,value)
    features[key]=value

df=pd.DataFrame(result.items())
df.to_csv('/home/leonardo/Scrivania/paziente_prova/CT_features_ptv_encefalo_bis.csv')

# Valutare se è possibile passare piú ROI contemporaneamente, ho visto su GoogleGroups che qualcuno ne ha parlato !!!
# A cosa potrebbe servire utilizzare params
# Capire cosa rappresentano le diverse features, estare le stesse per tutte le ROI? O cambiano? Se si in che modo perchè?
# C'è un numero massimo di features che pyradiomics riesce ad estrarre?
# Come pyradiomics classifica le diverse features?
# Capire anche il ruolo dei filtri!!!

# Le features vanno calcolate sull'immagine di dose (quindi è importante capire se(questo dipende dal dataset di Firenze) e come va utilizzato pyants)
# Attenzione ricordare che alcune features non dipendono dall'intensità
# Queste features possono darci delle info importanti su tossicità si / no;
# recidiva si / no  

# Rispetto alla dose che il radiologo ha previsto di dare, effettivamente quanta dose è arrivata su ciascuna struttura?
# (Potrebbero esserci dei problemi legati a movimento paziente, elettronica, ecc...)?????

