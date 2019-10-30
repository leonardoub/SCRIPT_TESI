#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:20:00 2019

@author: leonardo
"""


import radiomics
radiomics.setVerbosity(10)
import os
import numpy as np
import SimpleITK as sitk

dataDir = '/home/leonardo/pyradiomics/data'

Image_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/CT_2011-09-29_075800_TomoTherapy.Patient.Disease_kVCT.Image.Set_n232__00000'

Mask_path='/home/leonardo/Scrivania/paziente_prova/RT_nii'

#PER USARE PYRADIOMICS SERVONO IMMAGINI IN FORMATO COMPATIBILE CON SIMPLEITK. USARE sitk.ReadImage. IL PROBLEMA È CHE L'IMMAGINE CT È SPACCHETTATA IN TANTE IMMAGINI SI SINGOLE SLICE.
#CI SONO DELLE FUNZIONI DI SITK PER APRIRE I DICOM

#Carico immagine Mask

Maskstk=sitk.ReadImage(Mask_path+'/mask_ptv encefalo.nii')

#Carico immagine CT

Imagestk=sitk.ImageSeriesReader.GetGDCMSeriesFileNames(Image_path)
Imagestk=sitk.ReadImage(Imagestk)


#
#
##info_CT
#
#
#CT_size=Imagestk.GetSize()
#CT_spacing=Imagestk.GetSpacing()
#CT_depth=Imagestk.GetDepth()
#CT_dimension=Imagestk.GetDimension()
#CT_direction=Imagestk.GetDirection()
#CT_numberofpixels=Imagestk.GetNumberOfPixels()
#CT_origin=Imagestk.GetOrigin()
#
#
##info_ROI
#
#ROI_size=Maskstk.GetSize()
#ROI_spacing=Maskstk.GetSpacing()
#ROI_depth=Maskstk.GetDepth()
#ROI_dimension=Maskstk.GetDimension()
#ROI_direction=Maskstk.GetDirection()
#ROI_numberofpixels=Maskstk.GetNumberOfPixels()
#ROI_origin=Maskstk.GetOrigin()
#
##trasformo l'immagine CT in un Array e cerco il massimo
#
Image_np=sitk.GetArrayFromImage(Imagestk)
#a=np.max(Image_np)

Maskstk_np=sitk.GetArrayFromImage(Maskstk)
Maskstk_np[Maskstk_np==255]=1

A=Image_np*Maskstk_np

#b=A==1596


#c=Image_np[A==1597]

Media=np.mean(A) #non torna perchè bisggna dividere per il numero di voxel della ROI mentre qui probabilmente si divide per il numero di voxel dell'immagine
Max=np.max(A)
Min=np.min(A)



## i valori vengono uguali a quelli calcolati con lo scipt nostro! vedi meglio!

