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

Image_path='/home/leonardo/Documenti/Uni/Tesi/Retico/DATA/Patient01_RTplans/2015-08__Studies/Patient01_AIM01_RTDOSE_2015-08-10_112038_CSI.YW.PM_TomoTherapy.Planned.Dose_n1__00000/2.16.840.1.114362.1.11741058.22091046951.510100753.578.661.dcm'

Mask_path='/home/leonardo/Documenti/Uni/Tesi/Retico/DATA/Patient01_RTplans/RT_python_2015'

#PER USARE PYRADIOMICS SERVONO IMMAGINI IN FORMATO COMPATIBILE CON SIMPLEITK. USARE sitk.ReadImage. IL PROBLEMA È CHE L'IMMAGINE CT È SPACCHETTATA IN TANTE IMMAGINI SI SINGOLE SLICE.
#CI SONO DELLE FUNZIONI DI SITK PER APRIRE I DICOM

#Carico immagine Mask

Maskstk=sitk.ReadImage(Mask_path+'/mask_PTV midollo.nii')

#Carico immagine DOSE

#Imagestk=sitk.ImageSeriesReader.GetGDCMSeriesFileNames(Image_path)
Imagestk=sitk.ReadImage(Image_path)




#info_DOSE


DOSE_size=Imagestk.GetSize()
DOSE_spacing=Imagestk.GetSpacing()
DOSE_depth=Imagestk.GetDepth()
DOSE_dimension=Imagestk.GetDimension()
DOSE_direction=Imagestk.GetDirection()
DOSE_numberofpixels=Imagestk.GetNumberOfPixels()
DOSE_origin=Imagestk.GetOrigin()
DOSE_scaling=Imagestk.GetMetaData('3004|000e')

##Abbiamo usato GetMetaData (genera un dizionario) per accedere al DoseGridScaling, fattore di conversione tra valore del pixel e dose in Gy. '3004|000e' questa è la chiave a cui corrisponde il DGS
##GetMetaDataKeys genera una tupla di stringhe, noi lo abbiamo usato per capire quali sono le chiavi di GetMetaData

#info_ROI


ROI_size=Maskstk.GetSize()
ROI_spacing=Maskstk.GetSpacing()
ROI_depth=Maskstk.GetDepth()
ROI_dimension=Maskstk.GetDimension()
ROI_direction=Maskstk.GetDirection()
ROI_numberofpixels=Maskstk.GetNumberOfPixels()
ROI_origin=Maskstk.GetOrigin()

#radiomics.imageoperations.checkMask(Imagestk,Maskstk)
#Si può notare che lo spacing la direzione e l'origine di DOSE e ROI non coincidono
#Uniformiamo spacing direzione ed origine modificando la Mask

Maskstk.SetOrigin(DOSE_origin)
Maskstk.SetDirection(DOSE_direction)
Maskstk.SetSpacing(DOSE_spacing)

#radiomics.imageoperations.checkMask(Imagestk,Maskstk)

#Vediamo se ora la ROI e la DOSE sono uniformate

ROI_size1=Maskstk.GetSize()
ROI_spacing1=Maskstk.GetSpacing()
ROI_depth1=Maskstk.GetDepth()
ROI_dimension1=Maskstk.GetDimension()
ROI_direction1=Maskstk.GetDirection()
ROI_numberofpixels1=Maskstk.GetNumberOfPixels()
ROI_origin1=Maskstk.GetOrigin()



#
##Cercando di trovare i risultati così non funziona, forse è per il problema del label quindi si portano i valori della Mask da 255 a 1
#
Maskstk_np=sitk.GetArrayFromImage(Maskstk)
Maskstk_np[Maskstk_np==255]=1
Maskstk_1=sitk.GetImageFromArray(Maskstk_np)

#radiomics.imageoperations.checkMask(Imagestk,Maskstk_1)

#Imagestk_np=sitk.GetArrayFromImage(Imagestk)
#Imagestk_npa=Imagestk_np*float(DOSE_scaling)
#Imagestk_1=sitk.GetImageFromArray(Imagestk_npa)
####


DOSE_size1=Imagestk_1.GetSize()
DOSE_spacing1=Imagestk_1.GetSpacing()
DOSE_depth1=Imagestk_1.GetDepth()
DOSE_dimension1=Imagestk_1.GetDimension()
DOSE_direction1=Imagestk_1.GetDirection()
DOSE_numberofpixels1=Imagestk_1.GetNumberOfPixels()
DOSE_origin1=Imagestk_1.GetOrigin()

Imagestk_1.SetOrigin(DOSE_origin)
Imagestk_1.SetDirection(DOSE_direction)
Imagestk_1.SetSpacing(DOSE_spacing)

##Vediamo ora cosa succede all'immagine dopo essere stata trasformata in array e poi ritrasformata in un immagine
#
#
##le dimensioni, la direzione e altri parametri della ROI non sono cambiati
##invece l'origine della ROI e il voxel spacing della ROI sono cambiati purtroppo, quindi vanno riportati al valore originale
#
Maskstk_1.SetOrigin(DOSE_origin)
Maskstk_1.SetSpacing(DOSE_spacing)
Maskstk_1.SetDirection(DOSE_direction)




##Controlliamo che tutto sia tornato apposto (origine della ROI e il voxel spacing della ROI)
#
ROI_size2=Maskstk_1.GetSize()
ROI_spacing2=Maskstk_1.GetSpacing()
ROI_depth2=Maskstk_1.GetDepth()
ROI_dimension2=Maskstk_1.GetDimension()
ROI_direction2=Maskstk_1.GetDirection()
ROI_numberofpixels2=Maskstk_1.GetNumberOfPixels()
ROI_origin2=Maskstk_1.GetOrigin()


DOSE_size2=Imagestk_1.GetSize()
DOSE_spacing2=Imagestk_1.GetSpacing()
DOSE_depth2=Imagestk_1.GetDepth()
DOSE_dimension2=Imagestk_1.GetDimension()
DOSE_direction2=Imagestk_1.GetDirection()
DOSE_numberofpixels2=Imagestk_1.GetNumberOfPixels()
DOSE_origin2=Imagestk_1.GetOrigin()



#
#radiomics.imageoperations.checkMask(Imagestk_1,Maskstk_1)

#
###OK, tutto è tornato apposto!
###
###Cercando di trovare i risultati nemmeno così funziona, bisogna fare un'altra operazione ma non capisco perchè. Chiedere a Letizia!
###
##Per farla adattare la maschera si usa questa funzione: getMask: Function to get the correct mask. Includes enforcing a correct pixel data type (UInt32).
#
Maskstk_2=radiomics.imageoperations.getMask(Maskstk_1, label=1)

#radiomics.imageoperations.checkMask(Imagestk,Maskstk_2)


ROI_size2=Maskstk_2.GetSize()
ROI_spacing2=Maskstk_2.GetSpacing()
ROI_depth2=Maskstk_2.GetDepth()
ROI_dimension2=Maskstk_2.GetDimension()
ROI_direction2=Maskstk_2.GetDirection()
ROI_numberofpixels2=Maskstk_2.GetNumberOfPixels()
ROI_origin2=Maskstk_2.GetOrigin()




from radiomics import featureextractor

params = os.path.join('/home/leonardo/pyradiomics', "examples", "exampleSettings", "Params.yaml")

extractor=featureextractor.RadiomicsFeatureExtractor(params)
result=extractor.execute(Imagestk_1,Maskstk_2)

#ValueError: Image/Mask geometry mismatch. Potential fix: increase tolerance using geometryTolerance, see Documentation:Usage:Customizing the Extraction:Settings:geometryTolerance for more information


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
df.to_csv('/home/leonardo/Documenti/Uni/Tesi/Prove/2015/Risultati/features_dose_corretta_midollo_bis.csv')



#per verificare che Pyradiomics estrae delle cose vere provare a cercare il massimo (ad esempio nella regione del midollo) e vedere se corrisponde col massimo che trova lui. Usare numpy.where

