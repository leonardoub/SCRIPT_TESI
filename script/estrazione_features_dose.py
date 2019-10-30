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

#Carico immagine CT

#Imagestk=sitk.ImageSeriesReader.GetGDCMSeriesFileNames(Image_path)
Imagestk=sitk.ReadImage(Image_path)

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


#radiomics.imageoperations.checkMask(Imagestk,Maskstk)

#radiomics.imageoperations._correctMask(Imagestk,Maskstk)

from radiomics import featureextractor
#
#params = os.path.join('/home/leonardo/pyradiomics', "examples", "exampleSettings", "Params_correctMask.yaml")


extractor=featureextractor.RadiomicsFeatureExtractor(correctMask=True)
result=extractor.execute(Imagestk,Maskstk)

#proviamo a scrivere i risultati in un file csv

import pandas as pd

features={}

for key,value in result.items():
    features[key]=value

df=pd.DataFrame(result.items())
df.to_csv('/home/leonardo/Scrivania/paziente_prova/DOSE_features_Body.csv')





