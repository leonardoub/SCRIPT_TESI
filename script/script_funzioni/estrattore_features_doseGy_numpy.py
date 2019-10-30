#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:48:20 2019

@author: leonardo
"""


import numpy as np
import SimpleITK as sitk

def EstrattoreFeaturesDoseNp(Image_path,Mask_path,Output_path):
    
     Maskstk=sitk.ReadImage(Mask_path)
     Imagestk=sitk.ReadImage(Image_path)
     
     
     DOSE_size=Imagestk.GetSize()
     DOSE_spacing=Imagestk.GetSpacing()
     DOSE_depth=Imagestk.GetDepth()
     DOSE_dimension=Imagestk.GetDimension()
     DOSE_direction=Imagestk.GetDirection()
     DOSE_numberofpixels=Imagestk.GetNumberOfPixels()
     DOSE_origin=Imagestk.GetOrigin()
     DOSE_scaling=Imagestk.GetMetaData('3004|000e')

      
     Imagestk_np=sitk.GetArrayFromImage(Imagestk)
     Imagestk_np1=Imagestk_np*float(DOSE_scaling)
     Imagestk_1=sitk.GetImageFromArray(Imagestk_np1)
    
                 
     Imagestk_1.SetSpacing(DOSE_spacing)
     Imagestk_1.SetDirection(DOSE_direction)
     Imagestk_1.SetOrigin(DOSE_origin)
    
     DOSEnp=sitk.GetArrayFromImage(Imagestk_1)
     Masknp=sitk.GetArrayFromImage(Maskstk) 
     
     
     DOSEnp1=np.flip(DOSEnp,0)
     #serve per correggere la differente orientazione tra l'img della dose e l'immagine mask: è una inversione lungo l'asse z
     
     DOSEnp2=np.pad(DOSEnp1,((0,0),(23,25),(0,0)),'constant')
     #serve per riempire con degli zeri le righe mancanti all'img dose affinchè le img dose e img mask abbiano le stesse dimensioni lungo y
     
     DOSEnp3=DOSEnp2*Masknp

    
     S=np.sort(DOSEnp3, axis=None)
     #serve per creare un array monodimensionale e ordinato in senso crescente dalla matrice
     T=S[S.nonzero()]
     #vengono togli gli elementi nulli dal'array appena creato: erano moltissimi, così il valore minimo diverso da zero si trova all'indice zero
     
     Min=T[0]

     Max=np.max(DOSEnp3)

     Media=np.mean(T)

     stdv=np.std(T)

     return Min,Max,Media,stdv
     
     
     
     
     