#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:07:02 2019

@author: leonardo
"""
import radiomics
import SimpleITK as sitk
import os

radiomics.setVerbosity(10)

dataDir = '/home/leonardo/pyradiomics/data'

Image_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm' 

Mask_path='/home/leonardo/Scrivania/paziente_prova/RTst_nii'

#PER USARE PYRADIOMICS SERVONO IMMAGINI IN FORMATO COMPATIBILE CON SIMPLEITK. USARE sitk.ReadImage. IL PROBLEMA È CHE L'IMMAGINE CT È SPACCHETTATA IN TANTE IMMAGINI SI SINGOLE SLICE.
#CI SONO DELLE FUNZIONI DI SITK PER APRIRE I DICOM

#Carico immagine Mask

Maskstk=sitk.ReadImage(Mask_path+'/mask_Body.nii')

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

#info_ROI

#ROI_size=Maskstk.GetSize()
#ROI_spacing=Maskstk.GetSpacing()
#ROI_depth=Maskstk.GetDepth()
#ROI_dimension=Maskstk.GetDimension()
#ROI_direction=Maskstk.GetDirection()
#ROI_numberofpixels=Maskstk.GetNumberOfPixels()
#ROI_origin=Maskstk.GetOrigin()


#radiomics.imageoperations.checkMask(Imagestk,Maskstk)

#radiomics.imageoperations._correctMask(Imagestk,Maskstk)

Imagestk_np=sitk.GetArrayFromImage(Imagestk)
Imagestk_npa=Imagestk_np*float(DOSE_scaling)
Imagestk_1=sitk.GetImageFromArray(Imagestk_npa)

#DOSE_size1=Imagestk_1.GetSize()
#DOSE_spacing1=Imagestk_1.GetSpacing()
#DOSE_depth1=Imagestk_1.GetDepth()
#DOSE_dimension1=Imagestk_1.GetDimension()
#DOSE_direction1=Imagestk_1.GetDirection()
#DOSE_numberofpixels1=Imagestk_1.GetNumberOfPixels()
#DOSE_origin1=Imagestk_1.GetOrigin()
##DOSE_scaling1=Imagestk_1.GetMetaData('3004|000e')

Imagestk_1.SetSpacing(DOSE_spacing)
Imagestk_1.SetDirection(DOSE_direction)
Imagestk_1.SetOrigin(DOSE_origin)


from radiomics import featureextractor




#
#params = os.path.join('/home/leonardo/pyradiomics', "examples", "exampleSettings", "Params_correctMask.yaml")


radiomics.imageoperations.checkMask(Imagestk_1,Maskstk)

extractor=featureextractor.RadiomicsFeatureExtractor(correctMask=True)

radiomics.imageoperations.checkMask(Imagestk_1,Maskstk)

result=extractor.execute(Imagestk_1,Maskstk)


#proviamo a scrivere i risultati in un file csv

import pandas as pd

features={}

for key,value in result.items():
    features[key]=value

df=pd.DataFrame(result.items())
df.to_csv('/home/leonardo/Scrivania/paziente_prova/DOSE_features_Body_Gy_prova2.csv')


#SE LE COSE ESTRATTE SONO TUTTE LINEARI SI POSSONO MOLTIPLICARE I VALORI OTTENUTI PER IL DOSE GRID SCALING IN MODO DA OTTENERLI IN DOSE
#ANZICHÈ PASSARE DALL'IMMAGINE ALLA MATRICE, MOLTIPLICARE PER I DOSE GRID SCALING E POI OTTENERE DI NUOVO L'IMMAGINE DALLA MATRICE



