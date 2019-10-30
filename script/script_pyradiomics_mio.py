#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:07:02 2019

@author: leonardo
"""

import radiomics
import os
import numpy as np
import SimpleITK as sitk

dataDir = '/home/leonardo/pyradiomics/data'

Image_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/CT_2011-09-29_075800_TomoTherapy.Patient.Disease_kVCT.Image.Set_n232__00000'

Mask_path='/home/leonardo/Scrivania/paziente_prova'

#PER USARE PYRADIOMICS SERVONO IMMAGINI IN FORMATO COMPATIBILE CON SIMPLEITK. USARE sitk.ReadImage. IL PROBLEMA È CHE L'IMMAGINE CT È SPACCHETTATA IN TANTE IMMAGINI SI SINGOLE SLICE.
#CI SONO DELLE FUNZIONI DI SITK PER APRIRE I DICOM

#Carico immagine Mask

Maskstk=sitk.ReadImage(Mask_path+'/mask_ptv encefalo.nii')

#Carico immagine CT

Imagestk=sitk.ImageSeriesReader.GetGDCMSeriesFileNames(Image_path)
Imagestk=sitk.ReadImage(Imagestk)




#info_CT


#CT_size=Imagestk.GetSize()
#CT_spacing=Imagestk.GetSpacing()
#CT_depth=Imagestk.GetDepth()
#CT_dimension=Imagestk.GetDimension()
#CT_direction=Imagestk.GetDirection()
#CT_numberofpixels=Imagestk.GetNumberOfPixels()
#CT_origin=Imagestk.GetOrigin()


#info_ROI

#ROI_size=Maskstk.GetSize()
#ROI_spacing=Maskstk.GetSpacing()
#ROI_depth=Maskstk.GetDepth()
#ROI_dimension=Maskstk.GetDimension()
#ROI_direction=Maskstk.GetDirection()
#ROI_numberofpixels=Maskstk.GetNumberOfPixels()
#ROI_origin=Maskstk.GetOrigin()

#Cercando di trovare i risultati così non funziona, forse è per il problema del label quindi si portano i valori della Mask da 255 a 1

#Maskstk_np=sitk.GetArrayFromImage(Maskstk)
#Maskstk_np[Maskstk_np==255]=1
#Maskstk_1=sitk.GetImageFromArray(Maskstk_np)

#Vediamo ora cosa succede all'immagine dopo essere stata trasformata in array e poi ritrasformata in un immagine
#
#ROI_size1=Maskstk_1.GetSize()
#ROI_spacing1=Maskstk_1.GetSpacing()
#ROI_depth1=Maskstk_1.GetDepth()
#ROI_dimension1=Maskstk_1.GetDimension()
#ROI_direction1=Maskstk_1.GetDirection()
#ROI_numberofpixels1=Maskstk_1.GetNumberOfPixels()
#ROI_origin1=Maskstk_1.GetOrigin()


#le dimensioni, la direzione e altri parametri della ROI non sono cambiati
#invece l'origine della ROI e il voxel spacing della ROI sono cambiati purtroppo, quindi vanno riportati al valore originale

#Maskstk_1.SetOrigin(ROI_origin)
#Maskstk_1.SetSpacing(ROI_spacing)

#Controlliamo che tutto sia tornato apposto (origine della ROI e il voxel spacing della ROI)

#ROI_size1=Maskstk_1.GetSize()
#ROI_spacing1=Maskstk_1.GetSpacing()
#ROI_depth1=Maskstk_1.GetDepth()
#ROI_dimension1=Maskstk_1.GetDimension()
#ROI_direction1=Maskstk_1.GetDirection()
#ROI_numberofpixels1=Maskstk_1.GetNumberOfPixels()
#ROI_origin1=Maskstk_1.GetOrigin()

#OK, tutto è tornato apposto!

#Cercando di trovare i risultati nemmeno così funziona, bisogna fare un'altra operazione ma non capisco perchè. Chiedere a Letizia!

#Per farla adattare la maschera si usa questa funzione: getMask: Function to get the correct mask. Includes enforcing a correct pixel data type (UInt32).
#
#Maskstk_2=radiomics.imageoperations.getMask(Maskstk_1, label=1)
#
#ROI_size2=Maskstk_2.GetSize()
#ROI_spacing2=Maskstk_2.GetSpacing()
#ROI_depth2=Maskstk_2.GetDepth()
#ROI_dimension2=Maskstk_2.GetDimension()
#ROI_direction2=Maskstk_2.GetDirection()
#ROI_numberofpixels2=Maskstk_2.GetNumberOfPixels()
#ROI_origin2=Maskstk_2.GetOrigin()




from radiomics import featureextractor
extractor=featureextractor.RadiomicsFeatureExtractor()
result=extractor.execute(Imagestk,Maskstk)
#così funziona


#
#import radiomics
#result=radiomics.featureextractor.RadiomicsFeatureExtractor.execute(Imagestk,Maskstk_2)
##così non funziona
##TypeError: execute() missing 1 required positional argument: 'maskFilepath'


#
#from radiomics import featureextractor
#result=featureextractor.RadiomicsFeatureExtractor.execute(Imagestk,Maskstk_2)
##così non funziona
##TypeError: execute() missing 1 required positional argument: 'maskFilepath'

#NON CAPISCO PERCHÈ GLI ULTIMI DUE PEZZI NON SONO EQUIVALENTI AL PRECEDENTE???????

#proviamo a scrivere i risultati in un file csv

import pandas as pd

features={}

for key,value in result.items():
    features[key]=value

df=pd.DataFrame(result.items())
df.to_csv('/home/leonardo/Scrivania/paziente_prova/CT_features_ptv_encefalo_bis_tris.csv')





